FROM python:3.11-slim

WORKDIR /app

# requirements.txt 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 현재 폴더(myfast)의 모든 소스코드를 컨테이너 내부로 복사
COPY . .

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]