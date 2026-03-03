# 🤖 LangGraph Multi-Frontend Chatbot (Streamlit)

This project is a **multi-frontend AI chatbot system** built using **Streamlit** and **LangGraph**.  
It demonstrates how **multiple Streamlit frontends** can interact with **different LangGraph backends**, including **in-memory workflows** and **database-backed conversations**.

---

## 📁 Project Structure
langgraph-chatbot/
│
├── streamlit1_frontend_streaming.py          # Streamlit app 1 (uses langgraph1)
├── streamlit2_frontend_threading.py          # Streamlit app 2 (uses langgraph1)
├── streamlit3_frontend_databases.py          # Streamlit app 3 (uses langgraph2)
│
├── langgraph1_backend.py
│        
├── langgraph2.py
│  
├── requirements.txt       # Python dependencies
├── .gitignore
└── README.md



---

## 🔗 Frontend ↔ Backend Mapping

| Streamlit Frontend | Backend Used | Description |
|-------------------|-------------|-------------|
| `streamlit1_frontend_streaming.py` | `langgraph1_backend.py` | Streaming chat responses |
| `streamlit2_frontend_threading.py` | `langgraph1_backend.py` | Thread-based conversations |
| `streamlit3_frontend_databases.py` | `langgraph2_backend  .py` | Persistent chat using SQLite |

---

## ⚙️ Tech Stack

- **Python 3.10+**
- **Streamlit** – Chat UI
- **LangGraph** – Stateful LLM workflows
- **LangChain** – Message handling
- **SQLite** – Persistent chat storage
- **Groq / OpenAI** – LLM providers

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/langgraph-chatbot.git
cd langgraph-chatbot
```

### 2️⃣ Set Up Python Environment
```bash
python -m venv myenv
source myenv/bin/activate        # macOS / Linux
myenv\Scripts\activate           # Windows
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### Set Up Environment Variables
Create a `.env` file in the project root and add your API keys
```env
GROQ_API_KEY=your_groq_api_key
```

### Streaml Chat UI
Run the desired Streamlit frontend:
```bash
python -m streamlit run streamlit1_fontend_streaming.py
```

### Threaded Chat UI
```bash
python -m streamlit run streamlit2_fontend_treading.py
```

### Database Chat UI
```bash
python -m streamlit run streamlit3_fontend_databases.py
```