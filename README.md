# AI Research Assistant

An AI-powered Research Assistant that enables researchers, students, and professionals to interact with research papers using Retrieval-Augmented Generation (RAG). The application allows users to upload research papers, perform semantic search, generate summaries, compare multiple papers, create literature reviews, save research notes, and export research reports.

---

## Features

### Document Management
- Upload single or multiple PDF research papers
- Automatic PDF text extraction
- Intelligent text chunking
- Document indexing using vector embeddings
- Manage uploaded documents

### AI Research Assistant
- Chat with uploaded research papers
- Context-aware question answering
- Semantic document retrieval
- Multi-document querying

### Research Tools
- Paper Summary
- Methodology Extraction
- Key Contributions
- Limitations Analysis
- Future Work Extraction
- Practical Applications

### Research Analysis
- Compare multiple research papers
- Generate literature reviews
- Save research notes
- Export research reports

### Backend Services
- REST API using FastAPI
- Vector search using Qdrant
- Sentence Transformer embeddings
- Google Gemini integration
- Dockerized deployment

---

## Technology Stack

### Backend
- FastAPI
- Python
- Qdrant Vector Database
- Sentence Transformers
- Google Gemini API

### Frontend
- Streamlit

### Document Processing
- PyMuPDF
- Python Multipart

### Deployment
- Docker
- Docker Compose

---

## Project Structure

```text
ai-research-assistant/
│
├── app/
│   ├── api/
│   ├── services/
│   ├── schemas/
│   ├── database/
│   ├── models/
│   ├── utils/
│   ├── core/
│   ├── config.py
│   └── main.py
│
├── streamlit_app/
│   ├── Home.py
│   ├── pages/
│   └── config.py
│
├── uploads/
├── data/
│
├── Dockerfile.backend
├── Dockerfile.streamlit
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/<username>/ai-research-assistant.git

cd ai-research-assistant
```

---

### Create Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file.

Example:

```env
GEMINI_API_KEY=YOUR_API_KEY

HOST=0.0.0.0
PORT=8000

QDRANT_HOST=localhost
QDRANT_PORT=6333

MODEL_NAME=gemini-2.5-flash

API_URL=http://localhost:8000
```

---

## Running the Application

### Start Qdrant

```bash
docker run -p 6333:6333 qdrant/qdrant
```

### Start FastAPI

```bash
uvicorn app.main:app --reload
```

Backend:

```
http://localhost:8000
```

Swagger API:

```
http://localhost:8000/docs
```

### Start Streamlit

```bash
streamlit run streamlit_app/Home.py
```

Frontend:

```
http://localhost:8501
```

---

# Docker Deployment

Build and start all services:

```bash
docker compose up --build
```

Run in detached mode:

```bash
docker compose up -d
```

Stop containers:

```bash
docker compose down
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/upload/` | Upload research papers |
| GET | `/documents/` | List uploaded documents |
| POST | `/chat/` | Chat with selected documents |
| POST | `/compare/` | Compare research papers |
| POST | `/literature/` | Generate literature review |
| GET / POST | `/notes/` | Manage research notes |
| POST | `/export/` | Export research report |
| GET | `/dashboard/` | Dashboard statistics |

Interactive API documentation:

```
http://localhost:8000/docs
```

---

## Workflow

1. Upload one or more research papers.
2. Extract text and generate embeddings.
3. Store embeddings in Qdrant.
4. Retrieve relevant document chunks.
5. Generate responses using Google Gemini.
6. Save notes or export reports.

---

## Future Enhancements

- OCR support for scanned PDFs
- Citation generation
- Reference management
- User authentication
- Team collaboration
- Cloud storage integration
- Multi-language support
- Research recommendation engine
- Knowledge graph visualization


-Last deployment test using GitHub Actions.

---

## License

This project is intended for educational and research purposes.

---

## Author

**Priyanka Kumari**

AI Research Assistant using FastAPI, Streamlit, Qdrant, Sentence Transformers, and Google Gemini.
