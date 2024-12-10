from fastapi import FastAPI
from elasticsearch import Elasticsearch
import uvicorn
app = FastAPI()

url = "http://es8:9200/"

es = Elasticsearch(
    hosts=[url],
    verify_certs=False
)

@app.get('/')
async def root():
    if es.ping(): msg = 'connected by rithika🐯🐅🐯'
    else: msg='not connected'
    return {'message': msg}

