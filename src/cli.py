from ingest.text_loader import load_docker_docs
from ingest.chunker import chunk_documents
from embeddings.embedder import get_embedder
from ingest.build_index import build_index
from retriever.retriever import search_docker_docs
from chains.qa_chains import generate_answer
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
def main():
    docs=load_docker_docs()
    chunks=chunk_documents(docs)
    embedder=get_embedder()
    collection=build_index(chunks,embedder=embedder)
    llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
    )

    while True:
        query=input("\nAsk a Docker question( or 'exit try'): ")
        if query.lower()=="exit":
            break
        answer,sources=generate_answer(query=query,collection=collection,embedder=embedder,llm=llm)
        print("\nAnswer:",answer)
        print("\nSources:")
        for src in sources:
            print(f"--{src['metadata'].get('source','Unknown')}")

if __name__=="__main__":
    main()
