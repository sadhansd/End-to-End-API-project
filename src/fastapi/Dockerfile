FROM python:3.10-slim
WORKDIR /app
COPY src/fastapi/requirements.txt .
COPY ./src/fastapi/main.py .
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "8000"]