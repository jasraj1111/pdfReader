import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract all text from a PDF file."""
    text = ""
    try:
        with fitz.open(pdf_path) as pdf:
            for page in pdf:
                text += page.get_text("text") + "\n"
    except Exception as e:
        print(f"[ERROR] Failed to read PDF: {e}")
    return text.strip()
