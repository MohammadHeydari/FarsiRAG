# FarsiRAG  

A simple but powerful **Retrieval-Augmented Generation (RAG)** system for Persian language, built with:
- ParsBERT (for embeddings)
- ChromaDB (vector database)
- GapGPT / OpenAI-compatible API (LLM)
- Streamlit (chat UI)

---

## Features

- Fully supports Persian (Farsi) text
- Semantic search using ParsBERT embeddings
- Vector storage with ChromaDB
- LLM-powered answers (GapGPT / OpenAI-compatible API)
- Chat UI with Streamlit
- Simple and lightweight RAG pipeline (no LangChain dependency)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/FarsiRAG.git

cd FarsiRAG
```

2. Create virtual environment (recommended)

```
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

3. Install dependencies

```
pip install -r requirements.txt
```

If you don't have requirements.txt, install manually:

```
pip install hazm transformers torch chromadb langchain langchain-community openai streamlit
```

API Key Setup (IMPORTANT)

This project uses an OpenAI-compatible API (GapGPT).

You MUST provide your own API key.

Get your API key from:

https://gapgpt.app

Where to put the API key?

When running the app:

```
streamlit run app.py
```

You will see an input field:

```
GapGPT API Key
```

Paste your ```API key``` there.

How It Works:

1. Embedding
Uses ParsBERT to convert Persian text into vector embeddings.

2. Vector Database
Stores embeddings in ChromaDB.

3. Retrieval
Finds most relevant documents using semantic similarity.

4. Generation
Sends retrieved context to GapGPT / OpenAI API.
Generates final answer based only on context.

Add Your Own Data

Edit or extend ```rag/ingest.py```:

```
documents = [
    {
        "text": "Your Persian text here...",
        "metadata": {"source": "custom"}
    }
]
```

Then run:

```
python -m rag.ingest
```

Run the Project
1. Add documents
```
python -m rag.ingest
```
2. Start chat UI

```
streamlit run app.py
```

💬 Example Usage

Ask:

یادگیری عمیق چیست؟

Expected output:

یادگیری عمیق زیرمجموعه‌ای از یادگیری ماشین است که از شبکه‌های عصبی عمیق استفاده می‌کند.

Important Notes
-- You MUST provide a valid GapGPT API key
-- First run may download ParsBERT model (~600MB)
-- Internet required for model download
-- ChromaDB stores data locally in ./chroma_db

Requirements:

-- Python 3.9+
-- Internet connection (first run)
-- GapGPT API key

Troubleshooting
Problem: "No relevant documents found"

Run ingest first:

```
python -m rag.ingest
```

Problem: ```API error 401```

-- Your API key is invalid or missing
-- Make sure you paste it correctly in Streamlit UI

Problem: Slow first run

-- ParsBERT model is being downloaded (one-time only)

Future Improvements
-- Hybrid search (keyword + semantic)
-- FastAPI backend
-- Streaming responses
-- Conversation memory
-- Better reranking models
-- PDF / file upload support