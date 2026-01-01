# RAG Chatbot Backend

FastAPI backend for the Physical AI & Humanoid Robotics textbook with RAG (Retrieval-Augmented Generation) capabilities.

## Features

- **Chat Endpoint**: Ask questions about the book content
- **Selection Query**: Query based on user-selected text
- **Content Embedding**: Embed book chapters into Qdrant vector database
- **Conversation History**: Store chat history in Neon Postgres

## Setup

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Copy `env.example` to `.env` and fill in your credentials:

```bash
cp env.example .env
```

Required variables:
- `OPENAI_API_KEY`: Your OpenAI API key
- `QDRANT_URL`: Qdrant Cloud URL
- `QDRANT_API_KEY`: Qdrant API key
- `DATABASE_URL`: Neon Postgres connection string

### 3. Set Up Database

Run the schema SQL on your Neon Postgres database:

```bash
psql $DATABASE_URL < database/schema.sql
```

### 4. Embed Book Content

Run the embedding process to index all chapters:

```bash
python -m uvicorn main:app --reload
```

Then call the embedding endpoint:

```bash
curl -X POST http://localhost:8000/api/embed-content
```

### 5. Run the Server

```bash
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## API Endpoints

### Health Check
```
GET /api/health
```

### Chat
```
POST /api/chat
Body: {
  "message": "What is Physical AI?",
  "session_id": "optional-session-id"
}
```

### Query Selection
```
POST /api/query-selection
Body: {
  "selected_text": "Text selected by user",
  "question": "What does this mean?",
  "session_id": "optional-session-id"
}
```

### Embed Content
```
POST /api/embed-content
```

## Deployment

### Railway/Render

1. Create a new service
2. Connect your GitHub repository
3. Set environment variables
4. Deploy

The backend will be available at your deployment URL.

## Development

Run with auto-reload:

```bash
uvicorn main:app --reload
```

## Testing

Test the chat endpoint:

```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is ROS 2?"}'
```
