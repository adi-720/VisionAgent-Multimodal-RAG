# VisionAgent-Multimodal-RAG
A Multimodal RAG Assistant that understands documents and images using LangChain, ChromaDB, Groq LLM, and Groq Vision. VisionAgent is a Multimodal Retrieval-Augmented Generation (RAG) Assistant capable of processing both documents and images.

The system combines Large Language Models, Vision Models, Vector Databases, and Semantic Search to provide context-aware answers from uploaded content.

Users can upload documents and images, process them into a vector knowledge base, and ask natural language questions to retrieve relevant information.

## Features

- PDF Question Answering
- DOCX Support
- TXT Support
- Image Understanding
- Multimodal Retrieval-Augmented Generation (RAG)
- Semantic Search with ChromaDB
- Hugging Face Embeddings
- Groq LLM Integration
- Groq Vision Integration
- Source Citations
- Image Preview & Analysis
- Streamlit User Interface
- Context-Aware Question Answering
- Modular Architecture
- Future Ollama Integration Support

## Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI & Machine Learning
- LangChain
- Hugging Face Embeddings
- Groq LLM
- Groq Vision

### Vector Database
- ChromaDB

### Retrieval System
- Retrieval-Augmented Generation (RAG)
- Semantic Search

### Future Enhancements
- Ollama
- Local LLM Deployment
- Hybrid Search

## Installation

### Clone Repository

```bash
git clone https://github.com/adi-720/VisionAgent-Multimodal-RAG

cd VisionAgent-Multimodal-RAG
```

### Create Virtual Environment

```bash
python3 -m venv myenv
```

### Activate Environment

Mac/Linux

```bash
source myenv/bin/activate
```

Windows

```bash
myenv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

### Run Application

```bash
streamlit run src/streamlit_app.py
```
