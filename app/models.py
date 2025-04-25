from pydantic import BaseModel

class QuestionRequest(BaseModel):
    pdf_id: str
    question: str
