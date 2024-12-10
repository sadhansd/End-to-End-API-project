from elasticsearch import Elasticsearch

es = Elasticsearch(
    hosts=['http://localhost:9200/'],
    verify_certs=False
)

if es.ping():
    print("connected")
else:
    print("Failed")