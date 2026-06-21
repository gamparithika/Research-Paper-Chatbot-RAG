from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
# Load PDF
loader = PyPDFLoader("paper1.pdf")
documents = loader.load()

# Split text into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

texts = splitter.split_documents(documents)

# Embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-MiniLM-L3-v2",
    model_kwargs={"device": "cpu"}
)

# Create vector database
db = FAISS.from_documents(texts, embeddings)

# Save database
db.save_local("vectorstore")

print("Vector database created successfully!")

# Question loop
while True:
    question = input("\nAsk a question (type exit to stop): ")

    if question.lower() == "exit":
        break

    docs = db.similarity_search(question, k=3)

    print("\nRelevant Information:\n")

    for i, doc in enumerate(docs):
        print(f"Chunk {i+1}:")
        print(doc.page_content)
        print("-" * 80)