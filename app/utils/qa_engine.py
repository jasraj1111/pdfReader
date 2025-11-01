# qa_engine.py

from sentence_transformers import SentenceTransformer, util
import google.generativeai as genai
from dotenv import load_dotenv
import torch
import os
from .pdf_utils import extract_text_from_pdf


# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize embedder once
embedder = SentenceTransformer("all-mpnet-base-v2")

def find_relevant_context(question: str, text: str, top_k: int = 3) -> str:
    """
    Returns the top-k most semantically relevant chunks of text for the question.
    """
    # 1️⃣ Split into semantic chunks
    words = text.split()
    chunks = [" ".join(words[i:i+150]) for i in range(0, len(words), 150)]

    # 2️⃣ Embed chunks + question
    embeddings = embedder.encode(chunks, convert_to_tensor=True)
    q_emb = embedder.encode(question, convert_to_tensor=True)

    # 3️⃣ Compute similarity scores
    scores = util.cos_sim(q_emb, embeddings)

    # 4️⃣ Select top-k chunks
    top_indices = torch.topk(scores, k=min(top_k, len(chunks))).indices[0]
    selected_chunks = [chunks[i] for i in top_indices]

    # 5️⃣ Combine for model
    return "\n\n".join(selected_chunks)

def ask_question(text: str, question: str) -> str:
    """
    Finds relevant context and asks the Gemini model to answer the question.
    """
    context = find_relevant_context(question, text)

    model = genai.GenerativeModel("gemini-2.5-flash")
    chat = model.start_chat(history=[])

    prompt = f"""
    You are a professional AI assistant specializing in document analysis. Your goal is to provide clear, concise, and accurate answers.

    Follow these rules:
    1.  Analyze the user's question and the provided context carefully.
    2.  Formulate a direct and professional answer.
    3.  Use markdown for formatting (e.g., headings, bold text, and bullet points) to improve readability. 
        REMEMEBR -> The answer should not contain any kind of extra symbols or emojies like '*', '#', '`', '~' etc.
    4.  If the answer cannot be found within the context, you MUST state: "I could not find the answer to your question in the provided document."

    NOTE: Do not use external knowledge until the user says something like "Ezplain me in your way", this is where you can use your own knowledge to explain things in a simple way.

    ---
    # Context:
    {context}
    ---
    # Question:
    {question}
    """

    try:
        response = chat.send_message(prompt)
        return {
            "answer": response.text
        }
    except Exception as e:
        return {
            "answer": f"Error while generating answer: {str(e)}",
        }
