from fastapi import FastAPI
from pydantic import BaseModel
import transformers
from transformers import pipeline,AutoTokenizer, AutoModelForCausalLM
import pandas as pd
import sqlite3

# Set cuda if have
import torch
if torch.cuda.is_available():
    dev = "cuda"
else:
    dev = "cpu"
device = torch.device(dev)

# Init SQLite
conn = sqlite3.connect('casos.db')
c = conn.cursor()


excel_file = '../../database/bd_conocimiento.xlsx'
df = pd.read_excel(excel_file)

# Guarda en formato CSV
csv_file = '../../database/bd_conocimiento.csv'
df.to_csv(csv_file, index=False)



# Init Model
#reformulate = pipeline('text2text-generation', model='t5-base')


#phi_3 = AutoModelForCausalLM.from_pretrained("microsoft/Phi-3-mini-4k-instruct")
#phi_3_tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")


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

    answer = RAG(query)

    return answer

def RAG(query):

    # Step 1 Reformulate
    #enhance_query = reformulate(query, max_length=50)

    # Step 2 Can create SQL query?
    #messages = [{"role": "user", "content": query}]
    #inputs = phi_3_tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt")

    #outputs = phi_3.generate(inputs, max_new_tokens=32)
    #text = phi_3_tokenizer.batch_decode(outputs)[0]

        # Step 3 SQL query

        # Step 4 Retrieve k near "Acontecimiento"

            # Step 5 Reranking
        
    # Step 6 Answering

    return query

conn.commit()
conn.close()