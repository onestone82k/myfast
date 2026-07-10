from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
def get_message():
  return {"message":"안녕하세요. 백엔드 메세지 호출하셨죠?"}
