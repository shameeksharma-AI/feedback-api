from sqlalchemy import create_engine, Column, Integer, String, Boolean, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

Base = declarative_base()

class CallFeedback(Base):
    __tablename__ = "call_feedback"

    id = Column(Integer, primary_key=True, index=True)
    overall_experience = Column(String, nullable=False)   # good/moderate/bad
    audio_quality = Column(String, nullable=False)         # good/moderate/bad
    agent_helpful = Column(Boolean, nullable=False)
    issues_network = Column(Boolean, default=False)
    issues_loading = Column(Boolean, default=False)
    issues_audio_delay = Column(Boolean, default=False)
    issues_video_freeze = Column(Boolean, default=False)
    suggestions = Column(Text)
    submitted_at = Column(DateTime, default=datetime.utcnow)

DATABASE_URL = "sqlite:///./feedback.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)
