from sqlalchemy import Column, Integer, String
from src.config.database import Base

class Target(Base):
    __tablename__ = "tm_target"
    
    # 필수 식별자는 반드시 포함해야 함
    idx = Column(Integer, primary_key=True, index=True)
    
    # 필요한 필드만 선택적으로 선언
    biz_no = Column(String(10))
    corp_nm = Column(String(100))
    
    # (예시) 나머지 컬럼은 생략해도 SQLAlchemy가 에러를 내지 않습니다.