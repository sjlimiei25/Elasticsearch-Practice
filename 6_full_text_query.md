### 멀티 매치 쿼리
**가중치 부여**
```
GET kibana_sample_data_ecommerce/_search
{
  "_source": ["customer_first_name", "customer_last_name", "customer_full_name"],
  "query": {
    "multi_match": {
      "query": "mary",
      "fields": [
        "customer_first_name",
        "customer_last_name",
        "customer_full_name^2"
      ]
    }
  }
}
```

**와일드카드처리**
```
GET kibana_sample_data_ecommerce/_search
{
  "_source": ["customer_first_name", "customer_last_name", "customer_full_name"],
  "query": {
    "multi_match": {
      "query": "mary",
      "fields": [
        "customer_*_name"
      ]
    }
  }
}
```

```
GET kibana_sample_data_ecommerce/_search
{
  "_source": ["customer_first_name", "customer_last_name", "customer_full_name"],
  "query": {
    "multi_match": {
      "query": "mary",
      "fields": [
        "customer_first_name",
        "customer_last_name",
        "customer_full_name"
      ]
    }
  }
}
```

### 매치 프레이즈 쿼리
```
GET kibana_sample_data_ecommerce/_search
{
  "_source": ["customer_full_name"],
  "query": {
    "match_phrase": {
      "customer_full_name": "mary bailey"
    }
  }
}
```

### 매치 쿼리
**복수 개의 용어 검색 `Mary` `Bailey`**
```
GET kibana_sample_data_ecommerce/_search
{
  "_source": ["customer_full_name"],
  "query": {
    "match": {
      "customer_full_name": {
        "query": "mary bailey",
        "operator": "and"
      }
    }
  }
}
```

```
GET kibana_sample_data_ecommerce/_search
{
  "_source": ["customer_full_name"],
  "query": {
    "match": {
      "customer_full_name": "mary bailey"
    }
  }
}
```

**하나의 용어 검색 `Mary`**
```
GET kibana_sample_data_ecommerce/_search
{
  "_source": ["customer_full_name"],
  "query": {
    "match": {
      "customer_full_name": "Mary"
    }
  }
}
```
