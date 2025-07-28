from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .models import Show
from .database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/shows")
def read_shows(db: Session = Depends(get_db)):
    return db.query(Show).all()

@router.post("/shows")
def add_show(show: Show, db: Session = Depends(get_db)):
    db.add(show)
    db.commit()
    db.refresh(show)
    return show
