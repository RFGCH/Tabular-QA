from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

# Init FastAPI
app = FastAPI()

# Test API running
@app.get("/")
def read_root():
    return {"message": "Backend working"}

# Catch question
class QueryRequest(BaseModel):
    question: str

# Process question
@app.post("/ask")
def ask_question(request: QueryRequest):
    question = request.question
    answer = process_excel_query(question)
    return {"answer": answer}

# Process Excel & answer
def process_excel_query(query: str):

    df = pd.read_excel('../../database/bd_conocimiento.xlsx')
    
    # Lógica de procesamiento de la consulta
    if "total" in query.lower():
        total_value = df['Lugar'].sum()
        return f"El total es: {total_value}"
    
    return "Lo siento, no puedo responder a esa pregunta."

