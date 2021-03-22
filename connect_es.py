from elasticsearch import Elasticsearch

es = Elasticsearch(['localhost:9200'],http_auth=('elastic','RD7cgLg7XsflCJtH4j3O'))
res = es.search(index="kibana_sample_data_flights", body={"query":{"match_all":{}}})
for hit in res['hits']['hits']:
    print(hit["_source"])
