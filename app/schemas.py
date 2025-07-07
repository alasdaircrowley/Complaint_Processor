from pydantic import BaseModel
from datetime import datetime

class ComplaintCreate(BaseModel):
    text: str

class ComplaintResponse(BaseModel):
    id: int
    text: str
    timestamp: datetime
    status: str
    sentiment: str
    category: str

    class Config:
        orm_mode = True

    