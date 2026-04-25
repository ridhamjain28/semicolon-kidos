from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from datetime import datetime

class UserProfile(BaseModel):
    user_id: str = Field(..., example="child_001")
    age: int = Field(..., ge=5, le=13)
    interests: List[str] = []
    mastery_levels: Dict[str, float] = {} # e.g., {"space": 0.4, "dinosaurs": 0.8}
    curiosity_type: str = "exploratory"

class ContentItem(BaseModel):
    content_id: str
    title: str
    body: str
    tags: List[str]
    difficulty_score: float = Field(0.5, ge=0.0, le=1.0)
    curated_at: datetime = Field(default_factory=datetime.now)

class SignalModel(BaseModel):
    user_id: str
    signal_type: str # e.g., "skip", "duration", "text_feedback"
    value: float
    event_type: str # e.g., "interaction", "system_trigger"
    timestamp: datetime = Field(default_factory=datetime.now)
