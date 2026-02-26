from sqlalchemy import Column, Integer, String, DateTime
import datetime
from .db import Base

class AnalysisRecord(Base):
    __tablename__ = "analysis_records"

    id = Column(Integer, primary_key=True, index=True)
    code_snippet = Column(String)
    analysis_result = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
