### match 검색. beautiful
```
GET keyword_index/_search
{
  "query": {
    "match": {
      "contents": "beautiful"
    }
  }
}
```

```
GET keyword_index/_termvectors/1?fields=contents
```

### 도큐먼트 추가-> 인덱싱
```
PUT keyword_index/_doc/1
{
  "contents": "beautiful day"
}
```

### 'keyword_index' 인덱스 추가
- contents 필드 : keyword
```
PUT keyword_index
{
  "mappings": {
    "properties": {
      "contents": { "type": "keyword" }
    }
  }
}
```
