FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python -m spacy download en_core_web_lg
RUN pip install https://github.com/MartinoMensio/spacy-universal-sentence-encoder/releases/download/v0.4.6/en_use_lg-0.4.6.tar.gz#en_use_lg-0.4.6

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
