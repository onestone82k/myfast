from pydantic_settings import BaseSettings, SettingsConfigDict

# 1. OS 환경변수에서 'APP_ENV' 값을 읽어온다. (없으면 기본값: local)
env_state = os.getenv("APP_ENV", "local")

class Settings(BaseSettings):
  APP_NAME: str = "FastAPI App"
  DATABASE_URL: str
  # DATABASE_URL: str = "mysql+pymysql://pivotdev:djfudnsdkagh4$@mysql:3306/pivot"  
  JWT_SECRET: str
  
  # 2. env_state 값에 따라 읽어들일 파일을 동적으로 결정
  model_config = SettingsConfigDict(
    env_file=f".env.{env_state}",
    env_file_encoding="utf-8"
  )
 
settings = Settings()

