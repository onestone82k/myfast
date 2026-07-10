from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config.settings import settings

# 1. DB 엔진 생성 (MySQL 연결)
# pool_pre_ping=True: 연결이 끊겼을 때 자동으로 복구 시도
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20
)

# 2. 세션 생성 (DB와 한 번 통신할 때마다 필요한 세션 객체)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. 모델 클래스들이 상속받을 Base 클래스
Base = declarative_base()

# 4. FastAPI에서 사용할 DB 의존성 주입 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()