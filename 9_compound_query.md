### 복합쿼리 : 여러 쿼리를 조합하여 검색
#### - filter : 필터링하여 검색
```
GET kibana_sample_data_ecommerce/_search
{
  "_source": ["day_of_week", "customer_full_name"],
  "query": {
    "bool": {
      "filter": {
        "term": { "day_of_week": "Sunday" }
      },
      "must": {
        "match": { "customer_full_name": "mary" }
      }
    }
  }
}
```

```
GET kibana_sample_data_ecommerce/_search
{
  "_source": "products.base_price",
  "query": {
    "bool": {
      "filter": {
        "range": {
          "products.base_price": {
            "gte": 30,
            "lte": 60
          }
        }
      }
    }
  }
}
```

### - should : OR 연산
**다른 타입과 함께 사용**
```
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "bool": {
      "must": {
        "match": {"customer_full_name": "mary"}
      },
      "should": {
        "term": {"day_of_week": "Monday"}
      }
    }
  }
}
# => must 타입으로 검색된 결과에서
#    should 타입의 조건을 만족하는 문서에 스코어 점수를 더 부여
```

**복수의 쿼리 사용**
```
GET kibana_sample_data_ecommerce/_search
{
  "_source": ["customer_full_name", "day_of_week"],
  "query": {
    "bool": {
      "should": [
        {"match": {"customer_full_name": "mary"}},
        {"term": {"day_of_week": "Sunday"}}
      ]
    }
  }
}
```

**하나의 쿼리 사용**
```
GET kibana_sample_data_ecommerce/_search
{
  "_source": "customer_first_name",
  "query": {
    "bool": {
      "should": {
        "match": {"customer_first_name": "mary" }
      }
    }
  }
}
# => must 타입과 동일
```

### must_not : 문서에서 제외할 쿼리
**다른 타입과 함께 사용**
```
GET kibana_sample_data_ecommerce/_search
{
  "_source": "customer_full_name", 
  "query": {
    "bool": {
      "must": {
        "match": { "customer_first_name": "mary" }
      },
      "must_not": {
        "term": {"customer_last_name": "bailey" }
      }
    
  }
}
```

**하나의 쿼리 사용**
```
GET kibana_sample_data_ecommerce/_search
{
  "_source": "customer_first_name",
  "query": {
    "bool": {
      "must_not": {
        "match": { "customer_first_name": "mary" }
      }
    }
  }
}
```

### - must 
**복수의 쿼리 사용**
> customer_first_name 필드에 "mary"가 포함되고\
>   day_of_week 필드가 "Sunday"인 문서 검색
```
GET kibana_sample_data_ecommerce/_search
{
  "_source": ["customer_first_name", "day_of_week"],
  "query": {
    "bool": {
      "must": [
        {"match": {"customer_first_name": "mary"}},
        {"term" : {"day_of_week": "Sunday"}}
      ]
    }
  }
}
```
```
GET kibana_sample_data_ecommerce/_search
{
  "_source": ["customer_first_name", "day_of_week"],
  "query": {
    "bool": {
      "must": [
        {"match": {"customer_first_name": "mary"}},
        {"terms" : {"day_of_week": ["Sunday", "Monday"]}}
      ]
    }
  }
}
```

**하나의 쿼리 사용**
```
GET kibana_sample_data_ecommerce/_search
{
  "_source": "customer_first_name", 
  "query": {
    "bool": {
      "must": {
        "match": { "customer_first_name": "mary" }
      }
    }
  }
}
```
