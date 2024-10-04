# FROM python:3.8-slim-buster
FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["uvicorn", "startup:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["uvicorn", "startup:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
