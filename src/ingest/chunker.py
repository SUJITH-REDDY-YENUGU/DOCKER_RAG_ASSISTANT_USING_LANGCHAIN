
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(documents):
    """
    Chunks documents for efficient retrieval.
    
    CHUNKING STRATEGY:
    - chunk_size=1000: Captures complete Docker concepts (commands + explanations + examples)
      without fragmenting. Too small loses context, too large reduces retrieval precision.
    
    - chunk_overlap=200: 20% overlap preserves context at boundaries. Prevents information 
      loss when concepts span multiple chunks.
    
    - separators=["\n\n", "\n", ". ", " ", ""]: Hierarchical splitting at natural boundaries
      (paragraphs → lines → sentences → words) maintains readability and semantic coherence.
    """
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=1000,        # Optimal for complete concepts without diluting relevance
        chunk_overlap=200,      # 20% overlap to preserve cross-chunk context
        separators=["\n\n","\n",". "," ",""]  # Split at natural language boundaries
    )
    chunks=[]
    for doc in documents:
        for chunk in splitter.split_text(doc.page_content):
            chunks.append({"content":chunk,"metadata":doc.metadata})
    return chunks
