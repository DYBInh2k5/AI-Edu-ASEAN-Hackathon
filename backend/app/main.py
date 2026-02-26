from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.ai.ai_service import AIService
import logging

# Setup logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI(title="AI-Edu API")

# Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ai_service = AIService()

class CodeInput(BaseModel):
    code: str

@app.get("/")
def read_root():
    return {"message": "Welcome to AI-Edu API"}

@app.post("/analyze")
def analyze_code(input: CodeInput):
    logging.info(f"Analyzing code: {input.code[:50]}...")
    result = ai_service.analyze(input.code)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
