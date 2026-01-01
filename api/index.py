"""
Vercel Serverless Function Entry Point
This file adapts FastAPI for Vercel's serverless environment
"""
import sys
import os

# Add backend directory to path
backend_path = os.path.join(os.path.dirname(__file__), '..', 'backend')
sys.path.insert(0, backend_path)

# Change working directory to backend for relative imports
os.chdir(backend_path)

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv
from mangum import Mangum

# Load environment variables
load_dotenv()

app = FastAPI(title="Robotics Book RAG API")

# CORS middleware - update with your frontend URL
frontend_url = os.getenv("FRONTEND_URL", "https://hackathon-book-documnetation.vercel.app")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        frontend_url,
        "http://localhost:3000",
        "http://localhost:8000",
        "*",  # Allow all for development
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import request/response models
class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    session_id: str
    sources: List[str] = []

class SelectionQueryRequest(BaseModel):
    selected_text: str
    question: str
    session_id: Optional[str] = None

class TranslateRequest(BaseModel):
    text: str

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "robotics-book-rag"}

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Main chat endpoint using RAG"""
    try:
        from services.rag import RAGService
        
        rag_service = RAGService()
        response, sources = await rag_service.query(
            question=request.message,
            session_id=request.session_id
        )
        
        return ChatResponse(
            response=response,
            session_id=request.session_id or "default",
            sources=sources
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/query-selection", response_model=ChatResponse)
async def query_selection(request: SelectionQueryRequest):
    """Query based on selected text"""
    try:
        from services.rag import RAGService
        
        rag_service = RAGService()
        response, sources = await rag_service.query_with_context(
            question=request.question,
            context=request.selected_text,
            session_id=request.session_id
        )
        
        return ChatResponse(
            response=response,
            session_id=request.session_id or "default",
            sources=sources
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/translate")
async def translate(request: TranslateRequest):
    """Translate text to Urdu"""
    try:
        from services.rag import RAGService
        
        rag_service = RAGService()
        translated_text = await rag_service.translate_to_urdu(request.text)
        
        return {"translated_text": translated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/embed-content")
async def embed_content():
    """Embed all book content"""
    try:
        from services.embeddings import EmbeddingService
        
        embedding_service = EmbeddingService()
        result = await embedding_service.embed_all_chapters()
        
        return {"status": "success", "chunks_embedded": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Vercel handler - Mangum wraps FastAPI for AWS Lambda/Vercel compatibility
handler = Mangum(app, lifespan="off")

