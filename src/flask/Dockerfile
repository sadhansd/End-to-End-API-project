FROM python:3.10-slim
WORKDIR /app
COPY src/flask/requirements.txt .
COPY ./src/flask/app.py .
RUN pip install -r requirements.txt
CMD [ "python", "app.py" ]