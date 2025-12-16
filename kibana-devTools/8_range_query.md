### 범위 쿼리 (range query)
> kibana_sample_data_flights 인덱스 사용\
> =>날짜 검색 시 샘플 데이터를 추가한 기준일로 작성

**현재 시각 기준 한 달전까지의 문서 검색**
```
GET kibana_sample_data_flights/_search
{
  "_source": "timestamp",
  "query": {
    "range": {
      "timestamp": {
        "gte": "now-1M"
      }
    }
  }
}
```

**오늘 날짜 기준 검색 => 2025-12-12 <= x < 2025-12-13**
```
GET kibana_sample_data_flights/_search
{
  "_source": "timestamp", 
  "query": {
    "range": {
      "timestamp": {
        "gte": "2025-12-12",
        "lt": "2025-12-13"
      }
    }
  },
  "size": 10,
  "from": 2
}
# * 전체 결과 중 10개씩 보여줌
#   다른 데이터도 확인하고자할 경우 "from" 매개변수를 추가하여 가능!
```

**해당 인덱스의 매핑 정보 조회**
```
GET kibana_sample_data_flights/_mapping
```
