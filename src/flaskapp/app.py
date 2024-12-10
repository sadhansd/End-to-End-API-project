from flask import Flask
import requests
app = Flask(__name__)

URL = "http://fastapi-app:8000/"

@app.route('/')
def hello():
    try:
        response = requests.get(URL)
        data = response.json()
        return data['message']
    except:
        return "error"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)