import os
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_URL = "https://api.openai.com/v1/chat/completions"

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str
    model: str = "gpt-4o-mini"
    temperature: float = 0.7

@app.get("/")
def health_check():
    return {"status": "AI Engine running"}

@app.post("/generate")
def generate_text(data: PromptRequest):
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": data.model,
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": data.prompt}
        ],
        "temperature": data.temperature
    }

    response = requests.post(OPENAI_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail=response.text)

    result = response.json()
    return {
        "reply": result["choices"][0]["message"]["content"]
    }
