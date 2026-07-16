FROM python:3.11-slim

WORKDIR /app

# 시스템 의존성 설치 (MySQL 연결 등을 위해 필요할수있음)
RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev && rm -rf /var/lib/apt/lists/*

# requirements.txt 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 현재 폴더(backend)의 모든 소스코드를 컨테이너 내부로 복사
COPY . .

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]