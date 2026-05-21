# 📄 Local RAG Document Q&A with Llama 3

A fully local Retrieval-Augmented Generation (RAG) pipeline for document question-answering — no cloud API required. Upload any PDF and ask questions against it using a locally running Llama 3 model.

## Overview

This app implements a RAG pipeline entirely on local infrastructure. Documents are chunked, embedded using HuggingFace sentence transformers, stored in a FAISS vector store, and retrieved at query time to ground Llama 3's responses — eliminating hallucination on document-specific questions.

## Architecture

```
PDF Upload → Text Chunking → HuggingFace Embeddings → FAISS Vector Store
                                                              ↓
User Query → Similarity Search → Retrieved Chunks → Llama 3 (Ollama) → Answer
```

## Features

- Fully local — no OpenAI or cloud API costs
- RAG pipeline with FAISS vector store for fast semantic retrieval
- HuggingFace sentence-transformers for document embeddings
- Llama 3 Instruct via Ollama for answer generation
- Streamlit UI for PDF upload and interactive Q&A
- Supports any PDF document

## Tech Stack

- **LLM:** Llama 3 Instruct (via Ollama)
- **Embeddings:** HuggingFace sentence-transformers
- **Vector Store:** FAISS (CPU)
- **Orchestration:** LangChain
- **Frontend:** Streamlit

## Setup & Run

```bash
# Install Ollama and pull Llama 3
ollama pull llama3:instruct

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run main.py
```

## Project Structure

```
├── main.py              # Streamlit UI — file upload and query input
├── doc_chat_utils.py    # RAG pipeline — chunking, embedding, retrieval, QA chain
└── requirements.txt
```

## How It Works

1. User uploads a PDF via the Streamlit interface
2. Document is loaded and split into 1,000-token chunks with 200-token overlap
3. Chunks are embedded using HuggingFace sentence-transformers
4. Embeddings are stored in a FAISS in-memory vector store
5. User query is matched against chunks via cosine similarity
6. Top matching chunks are passed to Llama 3 via a RetrievalQA chain
7. Answer is returned and displayed in the UI
