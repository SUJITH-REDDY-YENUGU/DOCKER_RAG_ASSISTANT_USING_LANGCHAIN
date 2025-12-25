def search_docker_docs(query,collection,embedder,top_k=5):
    query_vector=embedder.embed_query(query)
    results=collection.query(
        query_embeddings=[query_vector],
        n_results=top_k,
        include=["documents","metadatas","distances"]

    )
    relevant_chunks=[]
    for i,doc in enumerate(results["documents"][0]):
        relevant_chunks.append({
            "content":doc,
            "metadata":results["metadatas"][0][i],
            "similarity":1-results["distances"][0][i]
        }

        )
    return relevant_chunks
