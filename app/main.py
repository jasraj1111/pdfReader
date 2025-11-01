from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uuid, os

from app.utils.pdf_utils import extract_text_from_pdf
from app.utils.qa_engine import find_relevant_context, ask_question
from app.utils.nlp_utils import preprocess_text, extract_keywords, summarize_text
from app.models import QuestionRequest

app = FastAPI()

# 🔐 Enable CORS
origins = [
    "http://localhost:5173",  # Vite default dev server
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 📁 Storage directories
PDF_DIR = "app/storage/pdfs"
TEXT_DIR = "app/storage/texts"
os.makedirs(PDF_DIR, exist_ok=True)
os.makedirs(TEXT_DIR, exist_ok=True)


# 📤 Upload PDF and extract + preprocess text
@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    pdf_id = str(uuid.uuid4())
    pdf_path = os.path.join(PDF_DIR, f"{pdf_id}.pdf")
    text_path = os.path.join(TEXT_DIR, f"{pdf_id}.txt")

    # Save PDF
    with open(pdf_path, "wb") as f:
        f.write(await file.read())

    # Extract text
    text = extract_text_from_pdf(pdf_path)

    # Preprocess + NLP insights
    clean_text = preprocess_text(text)
    summary = summarize_text(clean_text)
    keywords = extract_keywords(clean_text)

    # Store text for later question answering
    with open(text_path, "w", encoding="utf-8") as f:
        f.write(clean_text)

    return {
        "pdf_id": pdf_id,
        "message": "PDF uploaded and processed successfully.",
        "summary": summary,
        "keywords": keywords
    }


# ❓ Ask a question about the uploaded PDF
@app.post("/ask/")
async def ask_question_endpoint(request: QuestionRequest):
    text_path = os.path.join(TEXT_DIR, f"{request.pdf_id}.txt")

    if not os.path.exists(text_path):
        return JSONResponse(status_code=404, content={"error": "Document not found"})

    with open(text_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Find the most relevant context
    context = find_relevant_context(request.question, text)

    # Generate answer + confidence
    result = ask_question(context, request.question)

    return {
        "answer": result["answer"],
    }
