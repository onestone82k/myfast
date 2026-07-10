from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from src.config.database import get_db
from src.models import Target
from sqlalchemy.orm import Session

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"msg":"Hello World!"}


@app.get("/api/message")
def get_message(db: Session = Depends(get_db)):
    targets = db.query(Target).limit(10).all()
    return {"data": targets}
