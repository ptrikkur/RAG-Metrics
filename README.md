# RAG Pipeline with LlamaIndex and Qdrant

A complete Retrieval-Augmented Generation (RAG) pipeline implementation using LlamaIndex for orchestration and Qdrant as the vector database backend. This project demonstrates how to build a production-ready RAG system with document indexing, semantic search, optional reranking, and LLM-based generation.

## 🚀 Features

- **Document Ingestion**: Load and process documents from various sources (PDF, Markdown, Text)
  - *Tool*: `LlamaIndex SimpleDirectoryReader` - Automatic file format detection and loading
  
- **Vector Storage**: Efficient vector embeddings storage using Qdrant vector database
  - *Tool*: `Qdrant Client` + `QdrantVectorStore` - In-memory or persistent vector database
  
- **Semantic Search**: Fast similarity search using HuggingFace embeddings (BAAI/bge-small-en-v1.5)
  - *Tool*: `HuggingFaceEmbedding` from `llama-index-embeddings-huggingface` - 384-dimensional embeddings
  
- **Smart Chunking**: Configurable text chunking with overlap for better context preservation
  - *Tool*: `LlamaIndex Settings` - Built-in text splitter with configurable chunk size (512) and overlap (50)
  
- **Reranking**: Optional reranking using SentenceTransformer models for improved retrieval quality
  - *Tool*: `SentenceTransformerRerank` - Local reranking with BAAI/bge-reranker-base (no API key required)
  
- **LLM Integration**: Support for local LLMs via Ollama (llama3.2:1b)
  - *Tool*: `Ollama` from `llama-index-llms-ollama` - Local LLM inference without cloud APIs
  
- **Pure LlamaIndex**: No LangChain dependency - clean, modular architecture
  - *Tool*: `VectorIndexRetriever` + `RetrieverQueryEngine` - Native LlamaIndex components

## 📋 Prerequisites

- Python 3.12+ (tested with 3.12.2)
- Ollama (optional, for LLM generation)
- At least 4GB RAM for embedding models

## 🔧 Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd /path/to/VectorDB/RAG
   ```

2. **Install required packages:**
   ```bash
   pip install llama-index>=0.9.0
   pip install llama-index-vector-stores-qdrant>=0.1.0
   pip install llama-index-embeddings-huggingface>=0.1.0
   pip install qdrant-client>=2.7.0
   pip install sentence-transformers>=2.2.0
   pip install python-dotenv>=1.0.0
   pip install llama-index-llms-ollama  # For Ollama integration
   ```

3. **Set up environment variables:**
   Create a `.env` file in the project root:
   ```bash
   # Optional: For OpenAI or other API-based LLMs
   OPENAI_API_KEY=your_openai_api_key_here
   
   # Optional: For Cohere reranking (if using Cohere instead of SentenceTransformer)
   COHERE_API_KEY=your_cohere_api_key_here
   ```

4. **Install Ollama (optional, for local LLM):**
   ```bash
   # macOS
   brew install ollama
   
   # Start Ollama service
   ollama serve
   
   # Pull the llama3.2:1b model
   ollama pull llama3.2:1b
   ```

## 📁 Project Structure

```
RAG/
├── rag_pipeline.ipynb      # Main RAG pipeline implementation
├── .env                     # Environment variables (API keys)
├── docs/                    # Document directory for ingestion
│   ├── ai_fundamentals.md
│   ├── deep_learning.md
│   ├── machine_learning.md
│   ├── nlp.md
│   ├── vector_db_rag.md
│   └── dspy.pdf
├── models/                  # Cached embedding models
└── README.md               # This file
```

## 🎯 Quick Start

1. **Add your documents to the `docs/` folder:**
   - Supported formats: `.txt`, `.md`, `.pdf`
   - The pipeline will automatically load all files recursively

2. **Open and run the Jupyter notebook:**
   ```bash
   jupyter notebook rag_pipeline.ipynb
   ```

3. **Execute cells sequentially** to:
   - Initialize the vector database
   - Load embedding models
   - Index your documents
   - Set up the retriever
   - Test queries

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    RAG Pipeline Flow                         │
└─────────────────────────────────────────────────────────────┘

1. DOCUMENT INGESTION
   └─ Load documents from docs/ folder
   └─ Split into chunks (512 tokens, 50 token overlap)
   └─ Generate embeddings (BAAI/bge-small-en-v1.5, 384 dims)

2. VECTOR STORAGE (QDRANT)
   └─ Store embeddings in Qdrant vector database
   └─ Collection: "documents"
   └─ Distance metric: Cosine Similarity
   └─ In-memory mode (for testing) or persistent storage

3. QUERY PROCESSING
   └─ User query → Embedded using same model
   └─ Vector similarity search in Qdrant
   └─ Retrieve top 5 most similar documents

4. RERANKING (OPTIONAL)
   └─ SentenceTransformer reranking (BAAI/bge-reranker-base)
   └─ Refine results to top 3 most relevant
   └─ Runs locally - no API key required

5. GENERATION (OPTIONAL)
   └─ Feed retrieved context to LLM (Ollama/OpenAI)
   └─ LLM generates answer grounded in documents
   └─ Returns response + source citations
```

## ⚙️ Configuration

### Embedding Model
```python
embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5",
    cache_folder="./models"
)
```
- **Vector dimension**: 384
- **Model size**: ~133MB
- **Runs locally**: No API key required

### Chunking Strategy
```python
Settings.chunk_size = 512        # Tokens per chunk
Settings.chunk_overlap = 50      # Overlap between chunks
```

### Retrieval Settings
```python
retriever = VectorIndexRetriever(
    index=vector_index,
    similarity_top_k=5  # Number of documents to retrieve
)
```

### Reranking
```python
reranker = SentenceTransformerRerank(
    model="BAAI/bge-reranker-base",
    top_n=3  # Final number of documents after reranking
)
```

### LLM Configuration (Ollama)
```python
llm = Ollama(
    base_url="http://localhost:11434",
    model="llama3.2:1b",
    temperature=0.7,
    context_window=2048
)
```

## 🔍 Usage Examples

### Basic Retrieval (Without LLM)
```python
# Retrieve relevant documents
query = "What is machine learning?"
retrieved_nodes = retriever.retrieve(query)

for node in retrieved_nodes:
    print(f"Score: {node.score}")
    print(f"Text: {node.text[:100]}...")
```

### Full RAG with LLM Generation
```python
# Query with LLM generation
response = rag_query_engine.query("Explain RAG in simple terms")
print(response)

# Access source documents
for node in response.source_nodes:
    print(f"Source: {node.metadata.get('source')}")
```

## 📊 Sample Queries

The notebook includes test queries for:
- "What is machine learning?"
- "How does deep learning work?"
- "Tell me about vector databases"
- "What is RAG and why is it useful?"

## 🔑 Key Components

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Orchestration** | LlamaIndex | Document processing & query engine |
| **Vector DB** | Qdrant | Efficient vector storage & search |
| **Embeddings** | HuggingFace (BGE) | Semantic text embeddings |
| **Reranking** | SentenceTransformer | Improve retrieval relevance |
| **LLM** | Ollama (llama3.2:1b) | Generate natural language responses |

## 🎓 How It Works

### Query Embedding Process
**Yes, the retriever creates an embedding for the query!**

1. User submits a text query
2. Same embedding model (`BAAI/bge-small-en-v1.5`) converts query to 384-dim vector
3. Qdrant performs cosine similarity search against stored document embeddings
4. Top-k most similar documents are returned
5. Optional: Reranker refines the results
6. Optional: LLM generates answer using retrieved context

**Important**: The query and documents MUST use the same embedding model for meaningful similarity comparison.

## 🚦 Running the Pipeline

### Step-by-Step Execution

1. **Import Libraries** (Cell 1-2)
2. **Initialize Qdrant** (Cell 3) - Creates in-memory vector database
3. **Load Embeddings** (Cell 4) - Downloads and caches HuggingFace model
4. **Load Documents** (Cell 5) - Reads from `docs/` folder
5. **Create Index** (Cell 6) - Generates embeddings and stores in Qdrant
6. **Configure Reranking** (Cell 7) - Optional reranking setup
7. **Create Query Engine** (Cell 8) - Assembles the RAG pipeline
8. **Test Retrieval** (Cell 9) - Test without LLM generation
9. **Setup LLM** (Cell 10) - Configure Ollama
10. **Test Full RAG** (Cell 11) - Test with LLM generation

## 🐛 Troubleshooting

### Common Issues

**1. Model download fails:**
```bash
# Set HuggingFace cache directory
export HF_HOME=./models
```

**2. Ollama connection error:**
```bash
# Ensure Ollama is running
ollama serve

# Check if model is available
ollama list
```

**3. Out of memory errors:**
- Use smaller batch sizes
- Reduce `similarity_top_k` value
- Use a smaller embedding model

**4. No documents loaded:**
- Ensure documents exist in `../docs/` folder
- Check file permissions
- Verify supported file formats

## 📈 Performance Tips

1. **Use persistent Qdrant** for production:
   ```python
   qdrant_client = QdrantClient(url="http://localhost:6333")
   ```

2. **Adjust chunk size** based on your documents:
   - Smaller chunks (256): Better for precise information
   - Larger chunks (1024): Better for context-heavy queries

3. **Tune retrieval parameters**:
   - Increase `similarity_top_k` for broader context
   - Decrease for faster, more focused results

4. **Enable reranking** for improved accuracy (slight performance cost)

## 🔒 Security Notes

- Keep your `.env` file private (already in `.gitignore`)
- Never commit API keys to version control
- Use environment variables for all sensitive data
- For production, use proper secret management services

## 📝 License

This project is provided as-is for educational and development purposes.

## 🤝 Contributing

Suggestions and improvements are welcome! Consider:
- Adding support for more document formats
- Implementing hybrid search (keyword + semantic)
- Adding document metadata filtering
- Implementing response caching
- Adding evaluation metrics

## 📚 Resources

- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [Qdrant Documentation](https://qdrant.tech/documentation/)
- [HuggingFace Embeddings](https://huggingface.co/BAAI/bge-small-en-v1.5)
- [Ollama Documentation](https://ollama.ai/)

## ⚡ Next Steps

1. Load your own documents into the `docs/` folder
2. Experiment with different embedding models
3. Try different LLM providers (OpenAI, Anthropic, etc.)
4. Implement evaluation metrics for your use case
5. Deploy to production with persistent Qdrant instance

---

**Built with ❤️ using LlamaIndex and Qdrant**
