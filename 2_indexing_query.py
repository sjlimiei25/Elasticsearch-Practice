# 2_indexing_query.py
from elasticsearch import Elasticsearch

ES_HOST = "http://localhost:9200"
es = Elasticsearch([ES_HOST])

try:
  # * 인덱싱 : 인덱스에 문서를 포함시키는 것. 데이터 추가.
  # 데이터 준비. 추가될 문서.
  doc = {"name": "Kim", "age": 20}  # dict --> json

  # 인덱싱
  # res = es.index(index='test_index', body=doc)    # DeprecationWarning : 지원 중단 경고
  res = es.index(index='test_index', document=doc)  # body 옵션을 document 옵션으로 변경

  print('* ---- indexing ---- *')
  print(res)

  # * 인덱싱 후 바로 검색하기 위해 refresh
  es.indices.refresh(index='test_index')

  # * 쿼리 검색
  #   나이가 20살인 데이터 조회

  # - 검색 조건을 설정
  query = {
    "query": {
      "term": {
        "age": 20
      }
    }
  }
  # - 검색
  result = es.search(index='test_index', body=query)
  print('* ---- search ---- *')
  print(result)

except Exception as e:
  print('엘라스틱서치 인덱싱 중 예외 발생...')
  print(e)