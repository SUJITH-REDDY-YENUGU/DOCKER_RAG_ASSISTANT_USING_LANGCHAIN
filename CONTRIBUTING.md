
# Contributing to Docker RAG Assistant

Thank you for your interest in contributing! 
We welcome improvements, bug fixes, documentation updates, and new features. This guide will help you get started.

---

## 📋 How to Contribute

### 1. Fork & Clone
- Fork the repository on GitHub.  
- Clone your fork locally:
  ```bash
  git clone https://github.com/your-username/docker-rag-assistant.git
  cd docker-rag-assistant
  ```

### 2. Set Up Environment
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- Create a `.env` file in the root directory:
  ```bash
  GROQ_API_KEY=your_api_key_here
  EMBEDDING_MODEL=all-MiniLM-L6-v2
  CHUNK_SIZE=500
  CHUNK_OVERLAP=50
  ```

### 3. Branching
- Create a new branch for your changes:
  ```bash
  git checkout -b feature/your-feature-name
  ```

### 4. Code Style
- Follow **PEP8** guidelines for Python.  
- Keep dependencies minimal and list them in `requirements.txt`.  
- Add docstrings and comments for clarity.  

### 5. Testing
- Place tests in the `tests/` directory.  
- Run tests before submitting:
  ```bash
  pytest
  ```

### 6. Commit Messages
Use clear, descriptive commit messages:
```
feat: add retrieval evaluation script
fix: resolve chunk overlap bug
docs: update README with usage examples
```

### 7. Pull Requests
- Push your branch to GitHub:
  ```bash
  git push origin feature/your-feature-name
  ```
- Open a Pull Request (PR) against the `main` branch.  
- Clearly describe your changes and link related issues.  

---

## 🧩 Contribution Areas
You can help improve:
- Documentation (README, tutorials, visuals).  
- Retrieval evaluation and query processing.  
- Chunking strategy and overlap parameters.  
- Adding hybrid search or multi-turn conversation support.  
- Expanding datasets (e.g., Kubernetes, FastAPI docs).  

---

## ✅ Code of Conduct
By contributing, you agree to follow our `[Looks like the result wasn't safe to show. Let's switch things up and try something else!]`.  
Respectful communication and collaboration are expected at all times.

---

## 💡 Tips
- Keep PRs small and focused.  
- Ask questions in Issues if unsure.  
- Review existing discussions before opening new ones.  

---

