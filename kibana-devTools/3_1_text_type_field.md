### 'day' 용어 검색
```
GET text_index/_search
{
  "query": {
    "match": {
      "contents": "day"
    }
  }
}
```

### 'beautiful' 용어 검색
```
GET text_index/_search
{
  "query": {
    "match": {
      "contents": "beautiful"
    }
  }
}
```

### 'text_index' 인덱스에 도큐먼트(문서) 추가
- 1번 문서로 추가
```
PUT text_index/_doc/1
{
  "contents": "beautiful day"
}
```
> text 필드의 경우 용어 단위로 분리

**분리된 용어 정보 확인**
```
GET text_index/_termvectors/1?fields=contents
```

### 'text_index' 인덱스 추가
- contents 필드 : text
```
PUT text_index
{
  "mappings": {
    "properties": {
      "contents": { "type": "text" }
    }
  }
}
```
