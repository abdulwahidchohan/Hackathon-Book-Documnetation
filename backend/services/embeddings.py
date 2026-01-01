import os
import glob
from typing import List, Tuple
import google.generativeai as genai
import json

class EmbeddingService:
    def __init__(self):
        # Configure Gemini
        api_key = os.getenv("GEMINI_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
        
        self.embedding_model = 'models/text-embedding-004'
        self.chunk_size = 1000  # characters
        self.chunk_overlap = 200
        
    async def embed_all_chapters(self) -> int:
        """
        Embed all MDX files from docs/ directory
        Returns number of chunks embedded
        """
        # Get all MDX files
        docs_path = os.path.join(os.path.dirname(__file__), "../../docs")
        mdx_files = glob.glob(os.path.join(docs_path, "*.mdx"))
        mdx_files += glob.glob(os.path.join(docs_path, "*.md"))
        
        all_chunks = []
        all_embeddings = []
        all_metadata = []
        
        for file_path in mdx_files:
            print(f"Processing {os.path.basename(file_path)}...")
            chunks = self._chunk_file(file_path)
            
            for chunk_text, metadata in chunks:
                try:
                    # Generate embedding
                    embedding = self._generate_embedding(chunk_text)
                    
                    all_chunks.append(chunk_text)
                    all_embeddings.append(embedding)
                    all_metadata.append(metadata)
                    
                except Exception as e:
                    print(f"Error embedding chunk: {e}")
                    continue
        
        # Save to file
        self._save_embeddings(all_chunks, all_embeddings, all_metadata)
        
        return len(all_chunks)
    
    def _chunk_file(self, file_path: str) -> List[Tuple[str, dict]]:
        """
        Chunk a file into overlapping segments
        Returns list of (text, metadata) tuples
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract frontmatter
        title = os.path.basename(file_path)
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter = parts[1]
                content = parts[2]
                # Parse title from frontmatter
                title_line = [line for line in frontmatter.split('\n') if 'title:' in line]
                if title_line:
                    title = title_line[0].split('title:')[1].strip().strip('"\'')
        
        # Simple chunking by character count
        chunks = []
        start = 0
        while start < len(content):
            end = start + self.chunk_size
            chunk_text = content[start:end]
            
            # Skip very short chunks
            if len(chunk_text.strip()) < 100:
                break
            
            metadata = {
                "source": os.path.basename(file_path),
                "title": title,
                "start_char": start,
                "end_char": end
            }
            
            chunks.append((chunk_text, metadata))
            start += (self.chunk_size - self.chunk_overlap)
        
        return chunks
    
    def _generate_embedding(self, text: str) -> List[float]:
        """
        Generate embedding using Gemini
        """
        result = genai.embed_content(
            model=self.embedding_model,
            content=text,
            task_type="retrieval_document"
        )
        return result['embedding']
    
    def _save_embeddings(self, chunks: List[str], embeddings: List[List[float]], metadata: List[dict]):
        """
        Save embeddings to JSON file
        """
        data = {
            'chunks': chunks,
            'embeddings': embeddings,
            'metadata': metadata
        }
        
        with open('embeddings_cache.json', 'w', encoding='utf-8') as f:
            json.dump(data, f)
        
        print(f"Saved {len(chunks)} chunks to embeddings_cache.json")

