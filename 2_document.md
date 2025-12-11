### 'index2' 인덱스에서 1번 문서 삭제
```
DELETE index2/_doc/1
```

### 'index2' 인덱스에서 1번 문서의 
- name 필드의 값을 kim 으로 변경
```
POST index2/_update/1
{
  "doc": {
    "name": "kim"
  }
}
```

### 'index2' 인덱스에서 1번 문서 수정
```
PUT index2/_doc/1
{
  "name": "park",
  "age": 31
}
```

**추가된 문서 확인**
```
GET index2/_doc/1
```

### 'index2' 인덱스에서 5번 문서 조회
```
GET index2/_doc/5
```

### 'index2' 인덱스에 3번 문서 추가
- name, age, gender 필드
- age 데이터를 문자열 형태로 작성

**age 필드의 데이터를 문자열 형태로 작성**
```
PUT index2/_doc/3
{
  "name": "jihoon",
  "age": "31",
  "gender": "male"
}
```
```
PUT index2/_doc/4
{
  "name": "junyoung",
  "age": "29",
  "gender": "male"
}
```
**age 필드의 데이터를 실수 형태로 작성**
```
PUT index2/_doc/5
{
  "name": "hyungjin",
  "age": 39.9,
  "gender": "male"
}
```

### 'index2' 인덱스에 2번 문서 추가
- name 필드 (기존 필드)
- country 필드 (새로운 필드)

```
PUT index2/_doc/2
{
  "name": "jane",
  "country": "france"
}
```

### 전체 문서 조회
```
GET index2/_search
```

### 'index2' 인덱스 정보 조회
```
GET index2
```

### 'index2' 인덱스에 1번 문서 추가
```
PUT index2/_doc/1
{
  "name": "mike",
  "age": 25,
  "gender": "male"
}
```
