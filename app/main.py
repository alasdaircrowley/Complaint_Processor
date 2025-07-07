from fastapi import FastAPI, Depends, HTTPException
from fastapi.concurrency import run_in_threadpool
from sqlalchemy.orm import Session

from .database import SessionLocal, engine, Base
from . import models, schemas, sentiment, category

app = FastAPI()

Base.metadata.create_all(bind=engine)




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@app.post("/complaints", response_model=schemas.ComplaintResponse)
async def create_complaint(complaint: schemas.ComplaintCreate, db: Session = Depends(get_db)):

    new_complaint = models.Complaint(text=complaint.text)
    db.add(new_complaint)
    db.commit()
    db.refresh(new_complaint)

    sentiment_result = await sentiment.analyze_sentiment(complaint.text)
    category_result = await category.classify_category(complaint.text)

    new_complaint.sentiment = sentiment_result
    new_complaint.category = category_result
    db.commit()
    db.refresh(new_complaint)

    return new_complaint

@app.get("/complaints", response_model=list[schemas.ComplaintResponse])
def list_complaints(db: Session = Depends(get_db)):
    return db.query(models.Complaint).all()


