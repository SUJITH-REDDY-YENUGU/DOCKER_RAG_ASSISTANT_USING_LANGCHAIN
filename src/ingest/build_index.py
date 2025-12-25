# import chromadb

# def build_index(chunks,embedder,path="./vectordb/chroma"):
#     client=chromadb.PersistentClient(path=path)
#     collection=client.get_or_create_collection(
#         name="docker_docs",
#         metadata={"hnsw:space":"cosine"}

#     )
#     embeddings=embedder.embed_documents([c["content"] for c in chunks])
#     ids=[f"chunk{i}" for i in range(len(chunks))]
#     collection.add(
#         embeddings=embeddings,
#         ids=ids,
#         documents=[c["content"] for c  in chunks],
#         metadatas=[c["metadata"] for c in chunks]

#     )
#     return collection

import chromadb
from langchain_huggingface import HuggingFaceEmbeddings

def build_index(chunks, embedder,path="./vectordb/chroma"):
    # ✅ Use HuggingFace embeddings locally
    embedder = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Persistent ChromaDB client
    client = chromadb.PersistentClient(path=path)
    collection = client.get_or_create_collection(
        name="docker_docs",
        metadata={"hnsw:space": "cosine"}
    )

    print("Number of chunks:", len(chunks))  # Debug

    if not chunks:
        print("⚠️ No chunks provided. Check your loader/chunker.")
        return collection

    # Embed chunks with HuggingFace
    embeddings = embedder.embed_documents([c["content"] for c in chunks])
    ids = [f"chunk_{i}" for i in range(len(chunks))]

    # Add to Chroma collection
    collection.add(
        embeddings=embeddings,
        ids=ids,
        documents=[c["content"] for c in chunks],
        metadatas=[c["metadata"] for c in chunks]
    )

    print("Collections:", client.list_collections())
    return collection