from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(documents):
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n","\n",". "," ",""]
    )
    chunks=[]
    for doc in documents:
        for chunk in splitter.split_text(doc.page_content):
            chunks.append({"content":chunk,"metadata":doc.metadata})
    return chunks

