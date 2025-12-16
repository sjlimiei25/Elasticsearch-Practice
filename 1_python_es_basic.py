# 1_python_es_basic.py

# * 엘라스틱서치 모듈 설치 *
# > pip install elasticsearch

from elasticsearch import Elasticsearch

ES_HOST = 'http://localhost:9200'
es = Elasticsearch([ES_HOST]) 
# * 기본 주소(localhost:9200)인 경우 생략 가능 => Elasticsearch()

# 연결 확인
if es.ping():
  print('엘라스틱 서치 연결 성공')
else:
  print('엘라스틱 서치 연결 실패')
  print(es.info())      # 실패 시 내용 확인

# 실행 시 오류
# [1] 엘라스틱서치를 실행하지 않음 => Connected Error..
# [2] 엘라스틱서치 서비스와 모듈의 버전이 다름 => Unsupported Error..
#     > 설치했던 모듈 제거 : pip uninstall elasticsearch
#     > 버전을 지정해서 모듈 설치 : pip install elasticsearch==7.17.6