# Research-Paper-Chatbot-RAG
# 📚 Research Paper Chatbot (RAG)

A Retrieval-Augmented Generation (RAG) based chatbot that allows users to ask questions about research papers and retrieve relevant information from PDF documents using semantic search.

## 🚀 Features

- 📄 Load research papers in PDF format
- ✂️ Split text into chunks for efficient retrieval
- 🧠 Generate embeddings using Sentence Transformers
- 🔍 Store embeddings using FAISS vector database
- 💬 Ask questions and retrieve the most relevant text chunks
- ⚡ Fast semantic similarity search

---

## 🛠️ Technologies Used

- Python
- LangChain
- FAISS
- Hugging Face Sentence Transformers
- PyPDF
- RecursiveCharacterTextSplitter

---

## 📂 Project Structure

```
Research-Paper-Chatbot-RAG/
│
├── app.py
├── paper1.pdf
├── requirements.txt
├── README.md
│
└── vectorstore/
    ├── index.faiss
    └── index.pkl
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/gamparithika/Research-Paper-Chatbot-RAG.git

cd Research-Paper-Chatbot-RAG
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install langchain
pip install langchain-community
pip install langchain-text-splitters
pip install sentence-transformers
pip install faiss-cpu
pip install pypdf
```

---

## 📄 Add Your Research Paper

Place your PDF file inside the project directory.

Example:

```
paper1.pdf
```

---

## ▶️ Run the Project

```bash
python app.py
```

---

## 💬 Example

```
Vector database created successfully!

Ask a question (type exit to stop):

> What is the main contribution of the paper?

Relevant Information:

Chunk 1:
...
--------------------------------------------------------------------------------
Chunk 2:
...
--------------------------------------------------------------------------------
Chunk 3:
...
--------------------------------------------------------------------------------
```

---

## 🧠 Embedding Model Used

```python
sentence-transformers/paraphrase-MiniLM-L3-v2
```

---

## 📌 Future Improvements

- Support multiple PDF files
- Web interface using Streamlit
- LLM-powered answer generation
- Conversation memory
- Citation support
- Multi-document search
- Source highlighting

---

## 📸 Sample Output

```
Ask a question (type exit to stop):
> What is the abstract of the paper?

Relevant Information:

Chunk 1:
[Retrieved text from the research paper]
```

---

## 👩‍💻 Author

**Gampa Rithika**

- GitHub: https://github.com/gamparithika
- LinkedIn: www.linkedin.com/in/gampa-rithika-a291152a7

---

## ⭐ If you found this project useful, please give it a star!
