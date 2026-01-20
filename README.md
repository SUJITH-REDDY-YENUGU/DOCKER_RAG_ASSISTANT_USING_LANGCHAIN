
# Docker RAG Assistant

## Overview
The Docker RAG Assistant is a Retrieval-Augmented Generation (RAG) tool that helps developers quickly find answers from Docker documentation.  
Instead of manually browsing the Docker site, we collected key documentation pages, converted them into `.txt` files, and stored them in `data/raw/`.  
These files form the knowledge base for the assistant.

The assistant ingests these files, embeds them, and retrieves relevant sections to answer user queries with clear explanations and source citations.

---

## Problem
Docker documentation is large and often overwhelming. Developers waste time searching for commands, configuration details, or best practices.  
Keyword search doesn’t understand context, so results are often incomplete.

---

## Solution
Our assistant solves this problem by:
- Providing **direct answers** to natural language questions.
- Ensuring answers are **grounded in official Docker docs**.
- Saving developers time and improving productivity.

---

## Architecture
1. **Collect docs** → Docker documentation pages saved as `.txt` files.  
2. **Load docs** → Assistant reads the `.txt` files.  
3. **Chunk docs** → Split into smaller sections for efficient retrieval.  
4. **Embed chunks** → HuggingFace `all-MiniLM-L6-v2` embeddings.  
5. **Store in ChromaDB** → Vector database for semantic search.  
6. **Retrieve + Answer** → Relevant chunks passed to Groq’s LLM (`llama-3.1-8b-instant`) for answer generation.  
7. **Source citations** → Each answer cites the exact `.txt` files used.  

---

## Example Q&A

**Q:** What is Docker volume?  
**A:** A Docker volume is a way to persist data outside the lifecycle of a container. Even if the container is removed, the data remains.  
**Sources:** `docker_volume_overview.txt`, `docker_bind_mounts.txt`

---

**Q:** How does the VOLUME instruction in a Dockerfile work?  
**A:** The `VOLUME` instruction creates a mount point inside the container and marks it as holding externally mounted volumes.  
**Sources:** `dockerfile_reference.txt`

---

## Usage Instructions
1. Clone the repository.  
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
NOTE:ADD YOUR OWN GROQ API KEY TO LET IT WORK,OKAY?(YOU CAN GET IT )
3. Run the CLI:
   ```bash
   python src/cli.py
   ```
4. Ask questions like:
   ```
   What is Docker run?
   How do bind mounts differ from volumes?
   ```

---

## Repository Structure
```
src/
  ingest/        # loaders, chunker, build_index
  embeddings/    # embedder
  retriever/     # retriever logic
  chains/        # QA chain
  cli.py         # interactive CLI

data/
  raw/           # collected Docker docs in .txt files
  eval/          # optional evaluation Q/A pairs

notebooks/
  demo.ipynb     # demo notebook showing ingestion → query → answer

requirements.txt
README.md
LICENSE (optional)
```

---

## Future Work
- Add hybrid search (semantic + keyword).  
- Support multi-turn conversations with memory.  
- Expand dataset to include Kubernetes and FastAPI docs.  

---

## Impact
This assistant demonstrates how RAG can be applied to technical documentation.  
It reduces time spent searching, ensures accuracy by grounding answers in official docs, and provides a reproducible workflow for other domains.
```

---

### 📄 requirements.txt (as text)

```
chromadb==0.4.22
langchain
langchain-groq
sentence-transformers
python-dotenv
torch
transformers
tf-keras
```

---
