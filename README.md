
# 📄 Swiggy Report AI Assistant 

**GitHub Repo:** [https://github.com/mishra-khushboo/swiggy-rag-ai](https://github.com/mishra-khushboo/swiggy-rag-ai)

---

## 🔹 Project Description

This project is a **Retrieval-Augmented Generation (RAG) AI system** built to answer questions **directly from the Swiggy Annual Report**.  
It allows users to ask natural language questions and receive **accurate, context-grounded answers**. The system strictly uses the PDF content and **does not hallucinate**.

It is built with:

- **Python & Streamlit** – interactive web interface  
- **LangChain + FAISS** – vector store & semantic search  
- **HuggingFace Embeddings** – semantic similarity  
- **Transformers LLM (Flan-T5)** – answer generation  

---

## 🔹 Features

- ✅ Ask questions about Swiggy report  
- ✅ Suggested questions with one-click answers  
- ✅ Clickable PDF sentences to instantly ask AI  
- ✅ Highlight exact sentence from the PDF (Google-style)  
- ✅ Show source page numbers  
- ✅ Conversation memory (multi-turn, ChatGPT style)  
- ✅ Embedding visualization in 2D (semantic map)  

---

## 🔹 Screenshots

Here are some screenshots of the app in action:

![Home Page](https://github.com/mishra-khushboo/swiggy-rag-ai/blob/main/Screenshot%202026-03-06%20224315.png)  
![Suggested Questions](https://github.com/mishra-khushboo/swiggy-rag-ai/blob/main/Screenshot%202026-03-06%20224333.png)  
![Clicked Sentence QA](https://github.com/mishra-khushboo/swiggy-rag-ai/blob/main/Screenshot%202026-03-06%20224418.png)  
![Embedding Map](https://github.com/mishra-khushboo/swiggy-rag-ai/blob/main/Screenshot%202026-03-06%20224525.png)  

---

## 🔹 Installation

1. Clone the repo:

```bash
git clone https://github.com/mishra-khushboo/swiggy-rag-ai.git
cd swiggy-rag-ai
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Place the **Swiggy Annual Report PDF** in the repo folder and rename it to `swiggy_report.pdf`.

---

## 🔹 How to Run

```bash
streamlit run app.py
```

* Browser will open at `http://localhost:8501`
* Use suggested questions, enter your own questions, or click a PDF sentence
* View highlighted answers and page numbers
* Optional: click **“Show Embedding Map”** to visualize semantic relationships

---

## 🔹 Dataset

* **File:** `swiggy_report.pdf`
* **Source:** [Swiggy Investor Relations](https://www.swiggy.com/investor-relations)

> Make sure to mention this link when submitting to meet assignment requirements.

---

## 🔹 Project Structure

```
Swiggy_RAG_Assignment/
│
├── app.py                  # Main Streamlit + RAG code
├── requirements.txt        # All dependencies
├── README.md               # Project info & instructions
├── swiggy_report.pdf       # Dataset
├── screenshots/            # Optional screenshots of app
```

---

## 🔹 How This Project Stands Out

* Professional **RAG pipeline** with embeddings + vector store
* **Conversation memory** for multi-turn QA
* **Sentence highlighting & page citations** (like Google search)
* **Clickable PDF sentences** for instant answers
* **Embedding visualization** for a semantic map
* Fully interactive **Streamlit web app** for demonstrations



---

## 🔹 Author

**Khushboo Mishra** – IT & AI Enthusiast

* GitHub: [mishra-khushboo](https://github.com/mishra-khushboo)
   


