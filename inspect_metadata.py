"""
Demonstration: What metadata is stored with document chunks in LlamaIndex
"""

from llama_index.core import Document, VectorStoreIndex, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
import json

# Configure small chunks for demo
Settings.chunk_size = 100
Settings.chunk_overlap = 20

# Initialize embedding model
embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5",
    cache_folder="./models"
)

# Create sample document with known content
sample_doc = Document(
    text="""
    This is the first paragraph of my document. It contains important information about AI.
    
    This is the second paragraph. It discusses machine learning concepts and applications.
    
    This is the third paragraph. It covers deep learning and neural networks in detail.
    """,
    metadata={
        "file_name": "sample_document.txt",
        "author": "John Doe",
        "date": "2024-01-21",
        "category": "AI Education"
    }
)

# Create in-memory Qdrant
qdrant_client = QdrantClient(":memory:")
qdrant_client.create_collection(
    collection_name="demo",
    vectors_config=VectorParams(size=384, distance=Distance.COSINE)
)

vector_store = QdrantVectorStore(client=qdrant_client, collection_name="demo")

# Index the document (this will chunk it automatically)
vector_index = VectorStoreIndex.from_documents(
    documents=[sample_doc],
    vector_store=vector_store,
    embed_model=embed_model,
)

# Now let's inspect what was stored
print("=" * 80)
print("CHUNK METADATA INSPECTION")
print("=" * 80)

# Retrieve all nodes (chunks) from the index
retriever = vector_index.as_retriever(similarity_top_k=10)
results = retriever.retrieve("AI machine learning deep learning")

print(f"\nDocument was split into {len(results)} chunks\n")

for i, node in enumerate(results, 1):
    print(f"\n{'─' * 80}")
    print(f"CHUNK #{i}")
    print(f"{'─' * 80}")
    
    print(f"\n📄 TEXT CONTENT:")
    print(f"{node.text[:200]}..." if len(node.text) > 200 else node.text)
    
    print(f"\n📋 METADATA STORED:")
    for key, value in node.metadata.items():
        print(f"  • {key}: {value}")
    
    print(f"\n🔗 NODE ID: {node.node_id}")
    
    # Check for relationships
    if hasattr(node, 'relationships') and node.relationships:
        print(f"\n🔗 RELATIONSHIPS:")
        for rel_type, rel_info in node.relationships.items():
            print(f"  • {rel_type}: {rel_info}")
    
    # Score from retrieval
    if hasattr(node, 'score'):
        print(f"\n⭐ SIMILARITY SCORE: {node.score:.4f}")

print(f"\n{'=' * 80}")
print("KEY FINDINGS:")
print("=" * 80)
print("""
✅ WHAT IS STORED WITH EACH CHUNK:

1. ORIGINAL DOCUMENT METADATA
   - All metadata from the parent document (file_name, author, date, etc.)
   
2. CHUNK-SPECIFIC METADATA  
   - Node ID (unique identifier for each chunk)
   - Relationships (links to parent/previous/next chunks)
   
3. THE TEXT CONTENT
   - The actual chunk text
   
4. THE EMBEDDING VECTOR (in Qdrant)
   - 384-dimensional vector representation
   
5. ORDER INFORMATION
   - Through node relationships and IDs
   - Previous/Next chunk references maintained

🔗 LINK TO ORIGINAL DOCUMENT:
   YES! Through the metadata fields:
   - file_name, file_path, source, etc.
   - You can always trace back to the original document
""")
