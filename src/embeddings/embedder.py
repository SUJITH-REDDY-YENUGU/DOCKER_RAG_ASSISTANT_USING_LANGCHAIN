import torch
from langchain_huggingface import HuggingFaceEmbeddings

def get_embedder():
    device="cuda" if torch.cuda.is_available() else "cpu"
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device":device}
    )

