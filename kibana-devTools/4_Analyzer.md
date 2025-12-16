#### filter 테스트
```
POST _analyze
{
  "tokenizer": "standard",
  "filter": ["uppercase"],
  "text": "The 10 most loving dog breeds"
}
```

```
POST _analyze
{
  "tokenizer": "standard",
  "filter": ["lowercase"],
  "text": "The 10 most loving dog breeds"
}
```

#### tokenizer 테스트
```
POST _analyze
{
  "tokenizer": "uax_url_email",
  "text": "email: sjlim.iei.25@gmail.com"
}
```

```
POST _analyze
{
  "tokenizer": "standard",
  "text": "email: sjlim.iei.25@gmail.com"
}
```

#### analyzer 테스트
```
POST _analyze
{
  "analyzer": "stop",
  "text": "The 10 most loving dog breeds"
}
# => [most, loving, dog, breeds]
```

```
POST _analyze
{
  "analyzer": "simple",
  "text": "The 10 most loving dog breeds"
}
# => [the, most, loving, dog, breeds]
```

```
POST _analyze
{
  "analyzer": "whitespace",
  "text": "The 10 most loving dog breeds"
}
# => [The, 10, most, loving, dog, breeds]
```
### analyze API : 필터와 토크나이저 테스트 
