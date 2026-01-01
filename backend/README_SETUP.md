# RAG Backend Setup

## Gemini API Configuration

### 1. Get Your API Key
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click "Get API Key" or "Create API Key"
3. Copy your API key

### 2. Set Up Environment Variables

Create a `.env` file in the `backend` directory with:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

**Important:** Replace `your_actual_api_key_here` with your actual Gemini API key.

### 3. Current Model Configuration (2026)

The RAG system now uses:
- **Generation Model**: `gemini-2.0-flash-exp` - Fast, efficient model with multimodal support
- **Embedding Model**: `text-embedding-004` - Latest embedding model

### 4. Test the API

Run the test script to verify your API key works:

```bash
cd backend
python test_gemini.py
```

If successful, you should see a response explaining how AI works.

### 5. Start the Backend

```bash
cd backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 6. Embed Content

After starting the backend, embed your book content:

```powershell
Invoke-WebRequest -Uri "http://localhost:8000/api/embed-content" -Method POST
```

## Troubleshooting

### Error: "API key not valid"
- Make sure you copied the entire API key
- Check that there are no extra spaces in the `.env` file
- Verify the key is active in Google AI Studio

### Error: "Model not found"
- The models used are experimental/preview versions
- If `gemini-2.0-flash-exp` doesn't work, try:
  - `gemini-2.0-flash` (stable version)
  - `gemini-1.5-pro` (fallback)

### RAG Not Working
1. Check if embeddings are loaded: Look for `embeddings_cache.json` in backend folder
2. Run the embed-content endpoint to generate embeddings
3. Check backend logs for errors

## Model Alternatives

If you need to use different models, edit `backend/services/rag.py`:

```python
# For stable production use:
self.model = genai.GenerativeModel('gemini-2.0-flash')

# For more powerful responses:
self.model = genai.GenerativeModel('gemini-1.5-pro')

# For embeddings (if text-embedding-004 doesn't work):
self.embedding_model = 'models/embedding-001'
```
