FROM python:3.10-slim
WORKDIR /app
COPY src/flaskapp/requirements.txt .
COPY ./src/flaskapp/app.py .
RUN pip install -r requirements.txt
CMD [ "python", "app.py" ]