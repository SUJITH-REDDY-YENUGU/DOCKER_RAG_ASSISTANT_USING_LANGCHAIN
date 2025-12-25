from pathlib import Path
from langchain_community.document_loaders import TextLoader

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data" / "raw"

def load_docker_docs(path=DATA_DIR):
    documents = []
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Data directory not found: {path}")

    for file in path.iterdir():
        if file.suffix == ".txt":
            loader = TextLoader(
                file,
                encoding="utf-8"
            )
            documents.extend(loader.load())

    return documents
