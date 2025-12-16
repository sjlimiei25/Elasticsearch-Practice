### 용어들 쿼리 (terms query)
```
GET kibana_sample_data_ecommerce/_search
{
  "_source": ["day_of_week"],
  "query": {
    "terms": {
      "day_of_week": ["Monday", "Sunday"]
    }
  }
}
# * 어떤 문서의 day_of_week 필드가 "Monday" 추가 -> ["Monday"]
# * 검색어 ["Monday", "Sunday"] -> ["Monday", "Sunday"]
```

### 용어 쿼리 (term query)
**키워드 타입으로 지정하여 용어 쿼리**
```
GET kibana_sample_data_ecommerce/_search
{
  "_source": ["customer_full_name"],
  "query": {
    "term": {
      "customer_full_name.keyword": "Mary Bailey"
    }
  }
}

# * 해당  필드에 추가된 데이터 "Mary Bailey" -> ["Mary Bailey"]**
# * 검색어 "Mary Bailey" -> ["Mary Bailey"]
```

```
GET kibana_sample_data_ecommerce/_search
{
  "_source": ["customer_full_name"],
  "query": {
    "term": {
      "customer_full_name.keyword": "mary"
    }
  }
}
# * 해당  필드에 추가된 데이터 "Mary Bailey" -> ["Mary Bailey"]
# * 검색어 "mary" -> ["mary"]
```

**인덱스 매핑 정보 조회**
```
GET kibana_sample_data_ecommerce/_mapping
```
```
GET kibana_sample_data_ecommerce/_search
{
  "_source": ["customer_full_name"],
  "query": {
    "term": {
      "customer_full_name": "mary"
    }
  }
}
# * 문서 추가 후 구분된 용어 : ["mary", "bailey"]
# * term query 검색어 : ["Mary"]
```
```
GET kibana_sample_data_ecommerce/_search
{
  "_source": ["customer_full_name"],
  "query": {
    "term": {
      "customer_full_name": "Mary Bailey"
    }
  }
}
# * customer_full_name 필드에 "Mary Bailey" 추가했을 경우
#   용어 구분-> ["mary", "bailey"]

# * term query (검색) 시 검색어인 "Mary Bailey"는 탐색기 거치지 않음!
#   용어 -> ["Mary Bailey"]
```
