from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from feedback_db import SessionLocal, CallFeedback

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class FeedbackInput(BaseModel):
    overall_experience: str
    audio_quality: str
    agent_helpful: bool
    issues_network: bool = False
    issues_loading: bool = False
    issues_audio_delay: bool = False
    issues_video_freeze: bool = False
    suggestions: str = None

@app.post("/api/feedback/call")
def submit_call_feedback(feedback: FeedbackInput, db: Session = Depends(get_db)):
    fb = CallFeedback(
        overall_experience=feedback.overall_experience,
        audio_quality=feedback.audio_quality,
        agent_helpful=feedback.agent_helpful,
        issues_network=feedback.issues_network,
        issues_loading=feedback.issues_loading,
        issues_audio_delay=feedback.issues_audio_delay,
        issues_video_freeze=feedback.issues_video_freeze,
        suggestions=feedback.suggestions
    )
    db.add(fb)
    db.commit()
    db.refresh(fb)
    return {"status": "success", "message": "Feedback submitted", "id": fb.id}
