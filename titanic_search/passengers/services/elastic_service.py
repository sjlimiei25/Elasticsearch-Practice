from elasticsearch import Elasticsearch, helpers
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()
ES_HOST = os.getenv('ES_HOST')

class ElasticService:
    def __init__(self):
        self.index = 'titanic'
        self.es = Elasticsearch(ES_HOST)

        if not self.es.ping():
            self.es = None
            print(f'Elasticsearch Connection Failed.. ({ES_HOST})')
            return
        
        # TODO: 인덱스가 존재하지 않으면 create_index 메소드 실행
        if not None:
            pass
        
        # TODO: es.count()를 사용하여 현재 인덱스의 문서 개수 조회
        # TODO: 문서 개수가 0개라면 init_bulk_data() 실행하여 데이터 초기화
        res = None
        if res['count'] == 0:
            print('데이터 초기화 시작....')
            pass

    def init_bulk_data(self):
        '''
        init_bulk_data
        CSV 파일을 읽어서 Bulk API로 데이터 초기화
        '''
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))    # 현재 파일의 위치
            file_path = os.path.join(current_dir, 'train.csv')          # 현재 파일과 같은 위치의 trains.csv 경로

            df = pd.read_csv(file_path)
            # TODO: 결측치를 제거하여 df 변수에 할당
            df = None

            data_list = []
            for idx, row in df.iterrows():
                # TODO: 데이터 딕셔너리 생성하여 리스트에 추가
                #       hint: _index, _id, _source 키 필요
                data = {
                    # 작성 위치
                }
                data_list.append(data)
            
            # TODO: helpers.bulk를 사용하여 리스트의 데이터를 한 번에 삽입
            # TODO: 삽입 후 데이터를 바로 검색 가능하도록 인덱스 리프레쉬
            print(f'초기 데이터 초기화 완료 ')

        except Exception as e:
            print(f' 데이터 초기화 중 오류 발생: {e}')

    def search_passenger(self, params):
        # TODO: make_search_query를 통해 쿼리르 만들고, es.search 결과를 반환
        query = None
        return None

    def make_search_query(self, params):
        '''
        make_search_query
        전달된 params에 포함된 데이터를 기준으로 검색 쿼리를 생성
        
        :param params: 검색 조건에 대한 데이터
        {
          `name`: Name 필드에 대한 부분 일치 검색 단어,\\
          `gender`: Sex 필드에 대한 완전 일치 검색 단어,\\
          `survived`: Survived 필드에 대한 완전 일치 검색 단어 (0 또는 1),\\
          `size`: 검색 개수
        }
        '''
        must = []
        filter = []

        # TODO: params['name']이 있으면 Name 필드에 match 쿼리를 must에 추가
        if params.get('name'):
            pass

        # TODO: params['gender']가 있으면 Sex 필드에 term 쿼리를 filter에 추가
        if params.get('gender'):
            pass

        # TODO: params['survived]가 있으면 Survived 필드에 term 쿼리를 filter에 추가
        if params.get('survived') is not None:
            pass

        # TODO: bool 구조(must, filter)를 가진 최종 쿼리 딕셔너리 반환
        return {
            "query": {
                "bool": {
                    # 작성 위치
                }
            },
            "size": int(params.get('size', 10))
        }

    def create_index(self):
        # TODO: 인덱스 매핑을 정의하고, es.indices.create 호출
        mapping = {
            "properties": {
                "PassengerId": { "type": "integer"},
                "Name": {"type": "text", "fields": {"keyword": { "type": "keyword" }}},
                "Sex": { "type": "keyword"},
                "Survived": { "type": "integer"},
                # 필요한 필드 추가
            }
        }
        # 작성 위치
        print(f'인덱스 생성 완료: {self.index}')
        
elastic_service = ElasticService()
