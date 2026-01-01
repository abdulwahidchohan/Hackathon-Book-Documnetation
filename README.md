# Physical AI & Humanoid Robotics Textbook

**Hackathon Project**: Create a comprehensive textbook for teaching Physical AI & Humanoid Robotics with integrated RAG chatbot.

## 🎯 Project Overview

This project delivers:
- **Comprehensive Textbook**: 12 chapters covering Physical AI, ROS 2, NVIDIA Isaac, VLA models, and more
- **RAG Chatbot**: AI-powered assistant that answers questions about the book content
- **Modern Stack**: Docusaurus + FastAPI + Google Gemini 2.5-flash + Local Vector Cache

**Target Score**: 150 points (100 core + 50 bonus for Urdu translation)

## 📚 Book Content

### Priority Chapters (Fully Developed)
1. **Introduction to Physical AI & Humanoid Robotics** - Foundations, history, challenges
2. **ROS 2 Fundamentals** - Middleware, nodes, topics, services, Python integration

### Standard Chapters (Solid Outlines)
3. Hardware & Sensors
4. Perception & State Estimation  
5. Motion Planning & Control (NVIDIA Isaac)
6. Vision-Language-Action Models
7. AI-Native Software Development
8. Simulation & Tooling
9. Safety & Ethics
10. Case Studies & Benchmarks
11. Future Directions

All chapters include:
- ✅ APA citations (15+ total, 50%+ peer-reviewed)
- ✅ Code examples (Minimal Working Examples)
- ✅ Diagrams and figures
- ✅ Flesch-Kincaid grade 10-12 readability

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- Python 3.10+
- OpenAI API key
- Qdrant Cloud account (free tier)
- Neon Serverless Postgres (free tier)

### 1. Install Frontend Dependencies

```bash
npm install
```

### 2. Set Up Backend

```bash
cd backend
pip install -r requirements.txt
cp env.example .env
# Edit .env with your API keys
```

### 3. Configure Database

```bash
psql $DATABASE_URL < backend/database/schema.sql
```

### 4. Run Development Servers

**Frontend** (Terminal 1):
```bash
npm start
```

**Backend** (Terminal 2):
```bash
cd backend
python -m uvicorn main:app --reload
```

### 5. Embed Book Content

```bash
curl -X POST http://localhost:8000/api/embed-content
```

Visit `http://localhost:3000` to see the book!

## 🤖 RAG Chatbot Features

- **General Questions**: Ask anything about the book content
- **Text Selection Queries**: Select text and ask contextual questions
- **Conversation History**: Stored in Neon Postgres
- **Vector Search**: Powered by Qdrant for semantic search

### API Endpoints

```bash
# Health check
GET http://localhost:8000/api/health

# Chat
POST http://localhost:8000/api/chat
{
  "message": "What is Physical AI?",
  "session_id": "user123"
}

# Query selection
POST http://localhost:8000/api/query-selection
{
  "selected_text": "ROS 2 is built on DDS...",
  "question": "What is DDS?",
  "session_id": "user123"
}
```

## 📦 Deployment

### Frontend (GitHub Pages)

```bash
# Update docusaurus.config.ts with your GitHub details
npm run build
npm run deploy
```

### Backend (Railway/Render)

1. Create new service
2. Connect GitHub repo
3. Set environment variables:
   - `OPENAI_API_KEY`
   - `QDRANT_URL`
   - `QDRANT_API_KEY`
   - `DATABASE_URL`
4. Deploy!

## 🏗️ Project Structure

```
.
├── docs/                    # Book chapters (MDX)
│   ├── 01-introduction.mdx
│   ├── 02-ai-fundamentals.mdx
│   └── ...
├── backend/                 # FastAPI RAG backend
│   ├── main.py
│   ├── services/
│   │   ├── embeddings.py
│   │   └── rag.py
│   └── database/
│       └── schema.sql
├── src/                     # Docusaurus customization
│   └── css/
│       └── custom.css
├── static/                  # Static assets
│   └── img/
├── docusaurus.config.ts     # Docusaurus config
├── sidebars.ts              # Sidebar config
└── package.json             # Dependencies
```

## 🎨 Features

### Core (100 points)
- ✅ Comprehensive book content with citations
- ✅ Docusaurus deployment to GitHub Pages
- ✅ RAG chatbot with OpenAI + Qdrant + Neon
- ✅ Text selection-based queries
- ✅ Conversation history

### Bonus (50 points)
- ✅ **Urdu Translation**: Fully implemented dynamic translation using Gemini AI. Accessible via the "Urdu Translation" floating button on all documentation pages.

## 📖 Development Workflow

1. **Content**: Edit MDX files in `docs/`
2. **Backend**: Modify services in `backend/services/`
3. **Styling**: Update `src/css/custom.css`
4. **Test**: `npm start` and `uvicorn main:app --reload`
5. **Deploy**: `npm run deploy` and deploy backend

## 🧪 Testing

```bash
# Build test
npm run build

# Backend test
cd backend
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is ROS 2?"}'
```

## 📝 Citations

All chapters include proper APA citations from peer-reviewed sources:
- Macenski et al. (2022) - ROS 2 architecture
- Billard & Kragic (2019) - Robot manipulation
- Hwangbo et al. (2019) - Legged robot learning
- And 10+ more peer-reviewed sources

## 🤝 Contributing

This is a hackathon project, but contributions are welcome:
1. Fork the repo
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

[Add your license here]

## 🙏 Acknowledgments

Built with:
- [Docusaurus](https://docusaurus.io/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [OpenAI](https://openai.com/)
- [Qdrant](https://qdrant.tech/)
- [Neon](https://neon.tech/)

---

**Hackathon Submission**: Physical AI & Humanoid Robotics Textbook with RAG Chatbot
