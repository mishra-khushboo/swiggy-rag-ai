import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from transformers import pipeline
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np

st.title("📄 Swiggy Report AI Assistant (Pro Version)")

# -----------------------------
# Conversation Memory
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------------
# Load PDF
# -----------------------------
loader = PyPDFLoader("swiggy_report.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# -----------------------------
# Embeddings + VectorStore
# -----------------------------
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k":3})

# -----------------------------
# LLM Setup
# -----------------------------
llm = pipeline("text-generation", model="google/flan-t5-base", max_new_tokens=200)

# -----------------------------
# Helper Functions
# -----------------------------
def highlight_sentence(context, question):
    sentences = context.split(". ")
    for s in sentences:
        if any(word.lower() in s.lower() for word in question.split()):
            return "🔍 " + s.strip()
    return context[:200]

def ask_question(question):
    # Retrieve relevant chunks
    results = retriever.invoke(question)
    context = "\n".join([doc.page_content for doc in results])

    # Include conversation memory
    previous = "\n".join(st.session_state.history)
    prompt = f"""
Previous conversation:
{previous}

Context:
{context}

Question:
{question}

Answer:
"""
    answer = llm(prompt)[0]["generated_text"]

    # Update memory
    st.session_state.history.append(f"User: {question}")
    st.session_state.history.append(f"AI: {answer}")

    return answer, results

# -----------------------------
# Suggested Questions
# -----------------------------
st.subheader("💡 Suggested Questions")
suggested = [
    "What is Swiggy Instamart?",
    "What services does Swiggy offer?",
    "Who are Swiggy's competitors?",
    "What are Swiggy’s future plans?"
]
for q in suggested:
    if st.button(q):
        ans, sources = ask_question(q)
        st.write(ans)
        st.subheader("Sources & Pages")
        for doc in sources:
            st.write("Page:", doc.metadata.get("page", "N/A"))
            st.write(highlight_sentence(doc.page_content, q))

# -----------------------------
# User Input
# -----------------------------
st.subheader("Ask Your Own Question")
query = st.text_input("Enter your question")
if query:
    answer, sources = ask_question(query)
    st.subheader("📌 Answer")
    st.write(answer)
    st.subheader("Sources & Highlighted Evidence")
    for doc in sources:
        st.write("Page:", doc.metadata.get("page", "N/A"))
        st.write(highlight_sentence(doc.page_content, query))

# -----------------------------
# Clickable PDF Sentences
# -----------------------------
st.subheader("🖱 Click a sentence from PDF")
all_sentences = []
for doc in docs:
    sentences = doc.page_content.split(". ")
    for s in sentences:
        all_sentences.append((s, doc.metadata.get("page", 0)))

clicked_sentence = None
for sentence, page in all_sentences[:50]:  # limit 50 for UI speed
    if st.button(sentence[:50]+"..."):
        clicked_sentence = sentence

if clicked_sentence:
    answer, sources = ask_question(clicked_sentence)
    st.subheader("Selected Sentence")
    st.write(clicked_sentence)
    st.subheader("AI Answer")
    st.write(answer)
    st.subheader("Sources & Highlighted Evidence")
    for doc in sources:
        st.write("Page:", doc.metadata.get("page", "N/A"))
        st.write(highlight_sentence(doc.page_content, clicked_sentence))

# -----------------------------
# Embedding Visualization
# -----------------------------
if st.button("Show Embedding Map"):
    vectors = vectorstore.index.reconstruct_n(0, len(chunks))
    vectors = np.array(vectors)
    pca = PCA(n_components=2)
    reduced = pca.fit_transform(vectors)
    fig, ax = plt.subplots()
    ax.scatter(reduced[:,0], reduced[:,1])
    st.pyplot(fig)