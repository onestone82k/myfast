from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  APP_NAME: str = "FastAPI App"
  DATABASE_URL: str = "mysql+pymysql://pivotdev:djfudnsdkagh4$@52.79.138.161:3306/pivot"
  JWT_SECRET: str = "super-secret-key"

  class Config:
    env_file = ".env"   # .env 파일이 있으면 우선 로드

settings = Settings()

