from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
import json

from app.ai.ai_service import AIService
from app.models.db import SessionLocal, engine, get_db
from app.models.analysis import Base, AnalysisRecord
import logging

# Create tables
Base.metadata.create_all(bind=engine)

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
    allow_origins=["*"],
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
def analyze_code(input: CodeInput, db: Session = Depends(get_db)):
    logging.info(f"Analyzing code: {input.code[:50]}...")
    result = ai_service.analyze(input.code)
    
    # Save to Database
    record = AnalysisRecord(
        code_snippet=input.code,
        analysis_result=json.dumps(result)
    )
    db.add(record)
    db.commit()
    
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
