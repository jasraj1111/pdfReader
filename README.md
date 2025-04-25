📄 PDF Chatbot (FastAPI + React)
This project allows you to upload a PDF, and ask questions about its contents via a simple chat interface.

Built with:

⚡ FastAPI (Backend)

⚛️ React + Vite (Frontend)

🎨 CSS for simple styling

📄 PyMuPDF for PDF text extraction

✨ Features
Upload a PDF file.

Extracts the text from the PDF server-side.

Chat with the content: ask questions, get smart answers.

Clean and simple chat UI (React frontend).

Smooth integration between frontend and backend.

🛠️ Tech Stack

Frontend	Backend
React + Vite	FastAPI
Normal CSS	Python 3.11+
Fetch API	Uvicorn Server
📦 Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/pdf-chatbot.git
cd pdf-chatbot
2. Backend Setup (FastAPI)
bash
Copy
Edit
# Move into the backend directory if you have one, else stay at root
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate    # For Mac/Linux
# venv\Scripts\activate     # For Windows

# Install required libraries
pip install fastapi uvicorn python-multipart pypdf pymupdf
✅ Now start the FastAPI server:

bash
Copy
Edit
uvicorn main:app --reload --port 8000
3. Frontend Setup (React + Vite)
bash
Copy
Edit
# Move to frontend folder (or wherever you initialized React)
cd frontend

# Install dependencies
npm install

# Start the dev server
npm run dev
The React app will run at http://localhost:5173

⚙️ Project Structure
css
Copy
Edit
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
📸 Screenshots

Upload PDF & Chat
🧠 How it works
Upload a PDF → Saved in server /storage/pdfs/

Extract text → Saved in /storage/texts/

Ask a question → FastAPI loads text → Uses simple NLP or QA engine to generate an answer.

Return answer → Displayed beautifully in chat.

🛡️ License
This project is licensed under the MIT License.
Feel free to fork, modify and contribute! 🤝

🚀 Future Enhancements
Advanced AI (like OpenAI or local LLMs) for smarter answers.

History storage of chats.

PDF page navigation.

Multiple PDF upload handling.
