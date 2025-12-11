### 하위 타입 기준 쿼리
- contents 필드의 하위 타입 : keyword
```
GET multifield_index/_search
{
  "query": {
    "match": {
      "contents.keyword" : "day"
    }
  }
}
```
```
GET multifield_index/_termvectors/1?fields=contents.keyword
```

### 기본 타입 기준 쿼리
- contents 필드의 기본 타입 : text
```
GET multifield_index/_search
{
  "query": {
    "match": {
      "contents": "day"
    }
  }
}
```

#### * 기본 타입 : text
```
GET multifield_index/_termvectors/1?fields=contents
GET multifield_index/_termvectors/3?fields=contents
```

### 전체 문서 조회
```
GET multifield_index/_search
```

### 도큐먼트 인덱싱 -> 도큐먼트 추가
```
PUT multifield_index/_doc/1
{
  "message": "1 document",
  "contents": "beautiful day"
}

PUT multifield_index/_doc/2
{
  "message": "2 document",
  "contents": "beautiful day"
}

PUT multifield_index/_doc/3
{
  "message": "3 document",
  "contents": "wonderful day"
}
```

### 'multifield_index' 인덱스 생성
- message 필드 : text
- contents 필드 : text + keyword
```
PUT multifield_index
{
  "mappings": {
    "properties": {
      "message": { "type": "text" },
      "contents": { 
        "type": "text",
        "fields": {
          "keyword": { "type": "keyword" }
        }
      }
    }
  }
}
```
