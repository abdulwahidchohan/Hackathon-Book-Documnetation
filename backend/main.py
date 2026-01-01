from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Robotics Book RAG API")

# CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response models
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

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "robotics-book-rag"}

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Main chat endpoint using RAG
    """
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
    """
    Query based on selected text
    """
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

class TranslateRequest(BaseModel):
    text: str

@app.post("/api/translate")
async def translate(request: TranslateRequest):
    """
    Translate text to Urdu
    """
    try:
        from services.rag import RAGService
        
        rag_service = RAGService()
        translated_text = await rag_service.translate_to_urdu(request.text)
        
        return {"translated_text": translated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/embed-content")
async def embed_content():
    """
    Embed all book content into Qdrant
    This should be run once after content updates
    """
    try:
        from services.embeddings import EmbeddingService
        
        embedding_service = EmbeddingService()
        result = await embedding_service.embed_all_chapters()
        
        return {"status": "success", "chunks_embedded": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
