### 쿼리DSL 방식으로 요청
```
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "match": {
      "customer_full_name": "Mary"
    }
  }
}
```
> => "Mary" ---> "mary"

**특정 _id 문서의 customer_full_name 필드 용어 벡터 조회**
```
GET kibana_sample_data_ecommerce/_termvectors/qIT3D5sB_hFY90EMrmt8?fields=customer_full_name
```

### 쿼리스트링 방식으로 요청
```
GET kibana_sample_data_ecommerce/_search?q=customer_full_name:Mary
```

### kibana_sample_data_ecommerce 인덱스 매핑 정보 조회
```
GET kibana_sample_data_ecommerce/_mapping
```
