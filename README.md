# 📄 PDF Chatbot (FastAPI + React)

This project allows you to **upload a PDF**, and **ask questions** about its contents through a simple **chat interface**.

## Built with:
* ⚡ **FastAPI** (Backend)
* ⚛️ **React + Vite** (Frontend)
* 🎨 **CSS** for styling
* 📄 **PyMuPDF** for PDF text extraction

## ✨ Features
* Upload and process PDF files.
* Ask questions about the uploaded document.
* Clean, modern chat interface.
* Smooth backend-frontend integration.

## 🛠️ Tech Stack

| Frontend | Backend |
|----------|---------|
| React + Vite | FastAPI (Python) |
| Normal CSS | Uvicorn Server |
| Fetch API | PyMuPDF, FastAPI |

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pdf-chatbot.git
cd pdf-chatbot
```

### 2. Backend Setup (FastAPI)

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate  # Windows

# Install dependencies
pip install fastapi uvicorn python-multipart PyMuPDF
```

✅ Start the FastAPI server:

```bash
uvicorn main:app --reload --port 8000
```

### 3. Frontend Setup (React + Vite)

```bash
# Move to frontend directory (if split), else stay in project root
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

React app will run on http://localhost:5173.

## ⚙️ Project Structure

```
pdf-chatbot/
├── backend/
│   ├── app/
│   │   ├── pdf_utils.py
│   │   ├── qa_engine.py
│   │   └── models.py
│   ├── main.py
│   └── storage/
│       ├── pdfs/
│       └── texts/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Header.jsx
│   │   │   ├── Chat.jsx
│   │   │   ├── MessageInput.jsx
│   │   │   └── FileUpload.jsx
│   │   ├── App.jsx
│   │   └── index.css
│   └── vite.config.js
└── README.md
```

## 📸 Screenshots

### Upload PDF & Chat
![image](https://github.com/user-attachments/assets/b8f3c745-dc33-48d8-9062-88cfc9e4d683)


## 🧠 How it works
* **Upload PDF** ➔ Stored in `/storage/pdfs/`
* **Text extracted** ➔ Saved in `/storage/texts/`
* **Ask questions** ➔ Load the text, process it, and answer
* **Chat UI** ➔ Displays user and AI messages cleanly.

## 🚀 Future Improvements
* Connect to OpenAI, HuggingFace or custom LLMs.
* Add multi-file management.
* Enhance the chat experience (loader animations, error handling, etc.).
* Improve document search with embeddings.

## 🛡 License
This project is licensed under the **MIT License**. Feel free to fork, improve, and contribute! 🤝
