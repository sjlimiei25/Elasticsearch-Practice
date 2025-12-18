## 2025-12-18 실습문제 안내
> `2025-12-16` 실습 내용을 참고하여 다음 문제를 풀이해보자\
> 필요에 따라 구글링 등을 통한 추가 검색 가능 (단, AI를 활용한 정답 복사 등은 최대한 지양할 것.)

### 문제
`ElasticService` 클래스 내에 선언된 `TODO:` 주석 부분을 완성하여 엘라스틱서치 연동 로직을 구현하시오.

### `titanic` 인덱스 필드 구성
|필드명|필드타입|설명|
|:---|:---|:---|
|PassengerId|integer|탑승객ID|
|Survived|integer|생존여부(1:생존, 0:사망)|
|Pclass|integer|승객석 등급(1,2,3)|
|Name|멀티타입으로구성|이름|
||-기본타입:text||
||-추가타입:keyword||
|Sex|keyword|성별|
|Age|float|나이|
|Fare|float|요금|
|Embarked|keyword|탑승지|

---

## 사전 준비사항
### 필요 모듈 설치
> pip install elasticsearch python-dotenv pandas

### 환경 변수 설정
- 프로젝트 루트 폴더에 `.env` 파일을 생성하고 엘라스틱서치 호스트 정보 입력
```
ES_HOST=http://localhost:9200
```

### 데이터 파일 확인
- `train.csv` 파일이 해당 클래스 파일과 동일한 경로에 있는 지 확인

---

### hint
- match 쿼리 : 문장 내에서 용어를 분석하여 유사한 텍스트 확인
- term 쿼리 : 정확한 값이 일치하는 지 확인
- bool 쿼리 : `must` 와 `filter` 등을 적절히 조합하여 다중 조건 처리