### [1] 'index4' 인덱스 생성
### [2] 생성 후 매핑 설정
**[1] 인덱스 생성**
```
PUT index4
GET index4/_mapping
```

**[2] 매핑 설정**
```
PUT index4/_mapping
{
  "properties": {
    "age": { "type": "short" },
    "name": { "type": "text" },
    "gender": { "type": "keyword" }
  }
}
```

### 'index3' 인덱스 매핑 정보 조회
```
GET index3/_mapping
```

### 'index3' 인덱스 생성
- age 필드 : short
- name 필드 : text
- gender 필드 : keyword
```
PUT index3
{
  "mappings": {
    "properties": {
      "age": { "type": "short" },
      "name": { "type": "text" },
      "gender": { "type": "keyword" }
    }
  }
}
```


### 'index2' 인덱스의 매핑 정보 조회
```
GET index2/_mapping
```
