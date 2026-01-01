import os
from typing import List, Tuple, Optional
import google.generativeai as genai
import numpy as np
from datetime import datetime
import json

class RAGService:
    def __init__(self):
        # Configure Gemini
        api_key = os.getenv("GEMINI_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
        
        # Use latest Gemini models (as of 2026)
        # gemini-2.0-flash-exp: Fast, efficient model with multimodal support
        # text-embedding-004: Latest embedding model
        self.model = genai.GenerativeModel('models/gemini-2.5-flash')
        self.embedding_model = 'models/text-embedding-004'
        
        # Simple in-memory storage for embeddings
        self.chunks = []
        self.embeddings = []
        self.metadata = []
        
        # Load embeddings if they exist
        self._load_embeddings()
    
    def _load_embeddings(self):
        """Load embeddings from file if available"""
        try:
            if os.path.exists('embeddings_cache.json'):
                with open('embeddings_cache.json', 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.chunks = data.get('chunks', [])
                    self.embeddings = data.get('embeddings', [])
                    self.metadata = data.get('metadata', [])
        except Exception as e:
            print(f"Could not load embeddings: {e}")
    
    def _save_embeddings(self):
        """Save embeddings to file"""
        try:
            with open('embeddings_cache.json', 'w', encoding='utf-8') as f:
                json.dump({
                    'chunks': self.chunks,
                    'embeddings': self.embeddings,
                    'metadata': self.metadata
                }, f)
        except Exception as e:
            print(f"Could not save embeddings: {e}")
    
    async def query(self, question: str, session_id: Optional[str] = None) -> Tuple[str, List[str]]:
        """
        Query the RAG system using Gemini
        Returns (response, sources)
        """
        try:
            # If no embeddings loaded, use direct query
            if not self.chunks:
                return await self._direct_query(question), ["Direct Gemini response"]
            
            # Generate embedding for question
            question_embedding = self._embed_text(question)
            
            # Find most similar chunks
            top_chunks, sources = self._search_similar(question_embedding, top_k=3)
            
            # Build context
            context = "\n\n".join(top_chunks)
            
            # Generate response with Gemini
            response = self._generate_response(question, context)
            
            return response, sources
            
        except Exception as e:
            print(f"Error in query: {e}")
            # Fallback to direct query
            return await self._direct_query(question), ["Direct Gemini response"]
    
    async def query_with_context(self, question: str, context: str, session_id: Optional[str] = None) -> Tuple[str, List[str]]:
        """
        Query with user-selected context
        """
        try:
            response = self._generate_response(question, context)
            return response, ["User-selected text"]
        except Exception as e:
            print(f"Error in query_with_context: {e}")
            return f"Error: {str(e)}", []
    
    async def _direct_query(self, question: str) -> str:
        """Direct query to Gemini without RAG"""
        try:
            prompt = f"""You are an expert assistant for a Physical AI and Humanoid Robotics textbook.
            
Question: {question}

Please provide a clear, technical answer based on your knowledge of robotics, ROS 2, NVIDIA Isaac, and humanoid robotics."""
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def _embed_text(self, text: str) -> List[float]:
        """
        Generate embedding for text using Gemini
        """
        try:
            result = genai.embed_content(
                model=self.embedding_model,
                content=text,
                task_type="retrieval_query"
            )
            return result['embedding']
        except Exception as e:
            print(f"Error embedding text: {e}")
            return [0.0] * 768  # Return zero vector on error
    
    def _search_similar(self, query_embedding: List[float], top_k: int = 3) -> Tuple[List[str], List[str]]:
        """
        Find most similar chunks using cosine similarity
        """
        if not self.embeddings:
            return [], []
        
        # Calculate cosine similarities
        similarities = []
        for emb in self.embeddings:
            sim = self._cosine_similarity(query_embedding, emb)
            similarities.append(sim)
        
        # Get top k indices
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        # Get chunks and sources
        top_chunks = [self.chunks[i] for i in top_indices]
        sources = [f"{self.metadata[i].get('title', 'Unknown')} (score: {similarities[i]:.2f})" 
                  for i in top_indices]
        
        return top_chunks, sources
    
    def _cosine_similarity(self, a: List[float], b: List[float]) -> float:
        """Calculate cosine similarity between two vectors"""
        a = np.array(a)
        b = np.array(b)
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    
    def _generate_response(self, question: str, context: str) -> str:
        """
        Generate response using Gemini with context
        """
        try:
            prompt = f"""You are an expert assistant for a Physical AI and Humanoid Robotics textbook.
Answer questions based on the provided context from the book.
Be concise, technical, and accurate.

Context from the book:

{context}

Question: {question}

Please provide a clear, technical answer based on the context above."""
            
            response = self.model.generate_content(prompt)
            return response.text
            
        except Exception as e:
            return f"Error generating response: {str(e)}"

    async def translate_to_urdu(self, text: str) -> str:
        """Translate text to Urdu using Gemini"""
        try:
            prompt = f"""Translate the following technical text from a Physical AI and Humanoid Robotics textbook into accurate, professional Urdu. 
Keep technical terms like "ROS 2", "NVIDIA Isaac", "SLAM", "AI", "humanoid" in English or alongside their Urdu translation.
Return ONLY the translated text.

Text to translate:
{text}
"""
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error in translate_to_urdu: {e}")
            return f"Error: {str(e)}"
