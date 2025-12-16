# 3_bulk_api.py
#   => 한 번에 여러 작업을 수행하도록 기능을 제공

# 캐글 데이터셋 중 타이타닉 데이터 사용
# - DataFrame 형태로 타이타닉 데이터 로드
#   * DataFrame : pandas 데이터 타입
# 1) pandas 임포트
import pandas as pd

# 2) 캐글 데이터셋 다운로드 (train.csv)
# 3) csv 파일로부터 읽어오기 => pd.read_csv(파일경로)
try:
  df = pd.read_csv('train.csv')
except Exception as e:
  print('데이터셋 로드 중 예외 발생 ----- *')
  print(e)
  exit()      # 프로세스 종료

# 결측치 확인
print(df.isna().sum())
# - 결측치 제거 : dropna()
df = df.dropna()

# ------------------------------------
# 엘라스틱서치에 인덱싱
# - 엘라스틱서치 연결
from elasticsearch import Elasticsearch, helpers

try:

  ES_HOST = 'http://localhost:9200'
  es = Elasticsearch([ES_HOST])

  if not es.ping():   # 엘라스틱서치에서 응답이 없는 경우
    raise ConnectionError("엘라스틱서치 서버에 연결할 수 없음")

except Exception as e:
  print('엘라스틱서치 연결 실패 ---- *')
  print(e)
  exit()

# - 인덱싱
#   * 인덱스명 : titanic
#   * 기존에 동일한 이름의 인덱스가 존재할 경우 해당 인덱스 삭제
#     - 동일한 이름의 인덱스 존재 유무 : es.indices.exists(index)
#     - 인덱스 삭제 : es.indices.delete(index)
INDEX_NAME = 'titanic'
if es.indices.exists(index=INDEX_NAME): # 해당 인덱스가 존재하는 경우
  es.indices.delete(index=INDEX_NAME)
  print(f'기존 인덱스 삭제 ({INDEX_NAME})')

#   * 인덱스 생성
#     - 매핑 정보
#       PassengerId | integer
#       Survived    | integer
#       Pclass      | integer
#       Name        | text + keyword
#       Sex         | keyword
#       Age         | float
#       Fare        | float
#       Embarked    | keyword
mapping = {
  "properties": {
    "PassengerId": { "type": "integer"},
    "Survived": { "type": "integer"},
    "Pclass": { "type": "integer"},
    "Name": {
      "type": "text",
      "fields": {
        "keyword": { "type": "keyword" }
      }
    },
    "Sex": { "type": "keyword"},
    "Age": { "type": "float"},
    "Fare": { "type": "float"},
    "Embarked": { "type": "keyword"}
  }
}
#   - 인덱스 생성 : es.indices.create
es.indices.create(index=INDEX_NAME, mappings=mapping)
print(f'인덱스 생성 완료: {INDEX_NAME}')
# --------------------------------------------------

# 문서 추가 (Bulk API)
# - 요청 시 데이터 타입 : dict
# - 데이터셋으로부터 읽어온 데이터 타입 : DataFrame

# DataFrame -> dict
data_list = []
for index, row in df.iterrows():    # iterrows() : (index, Series). 한 행씩 리턴
  data = {
    "_index": INDEX_NAME,
    "_source": row.to_dict(),       # to_dict() : dict 타입으로 변환
    "_id": row['PassengerId']       # _id 는 PassengerId 값으로 지정
  }
  data_list.append(data)

# bulk api 사용
success, error = helpers.bulk(es, data_list)
print(f'문서 추가 완료. (성공: {success}, 실패: {error})')

# * 추가 후 바로 검색하기 위해 refresh
es.indices.refresh(index=INDEX_NAME)

# * 여성 탑승객 정보만 조회 * ------------
#   출력 예)
#   - 이름: xxx, 나이: xx, 생존여부: 생존 또는 사망
query = {
  "query": {
    "term": {
      "Sex": "female"
    }
  },
  "size": 30,
  "from": 2
}

result = es.search(index=INDEX_NAME, body=query)
print('* ---- 여성 탑승객 정보 ---- *')
# print(result, type(result))
print(f"= 검색결과 총 개수: {result['hits']['total']['value']}")

passenger_list = result['hits']['hits']     # => 리스트 형태 []. 검색 결과 목록
# print(type(passenger_list))
for data in passenger_list:
  name = data['_source']['Name']
  age = data['_source']['Age']
  # survived = "생존" if data['_source']['Survived'] == 1 else "사망"
  if data['_source']['Survived'] == 1:
    survived = "생존"
  else:
    survived = "사망"

  print(f' - 이름: {name}, 나이: {age}, 생존여부: {survived}')