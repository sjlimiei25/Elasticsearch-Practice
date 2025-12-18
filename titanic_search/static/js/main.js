// DOM 로드 후
document.addEventListener('DOMContentLoaded', ()=>{  
  // form 기본 동작 방지
  const form = document.getElementById('form-search');
  form.addEventListener('submit', (e)=>{e.preventDefault()})

  // 검색 입력창에서 엔터 입력 시 검색 요청
  const keyword = document.getElementById('keyword');
  keyword.addEventListener('keydown', (e)=>{
    if (e.key == 'Enter') {
      searchPassengers();
    }
  })
});

function getSearchParams(form) {
  const formData = new FormData(form);
  const params = new URLSearchParams();

  for (const [key, value] of formData.entries()) {
    if (key === 'gender') {
      if (value === 'male' || value === 'female') {
        params.append(key, value);
      }
    } 
    else if (key === 'survived') {
      if (value === '0' || value === '1') {
        params.append(key, value);
      }
    } 
    else {
      // 다른 필드(keyword, ..)는 값이 있을 경우 그대로 전달
      if (value.trim() !== '') {
        params.append(key, value);
      }
    }
  }

  // 검색 개수 조건 추가
  const size = document.getElementById('search-size').value;
  params.append('size', size);

  return params.toString();
}

function searchPassengers() {
  const form = document.getElementById('form-search');
  const params = getSearchParams(form);
  

  fetch(`/search?${params}`)
    .then(response => response.json())
    .then(data => {
      const resultBody = document.getElementById('search_result');

      resultBody.innerHTML = '';

      data['list'].forEach(p => {
        const tr = document.createElement('tr');

        tr.innerHTML = `
          <td>${p.Name}</td>
          <td>${p.Age}</td>
          <td>${p.Sex}</td>
          <td>${p.Embarked}</td>
          <td>${p.Survived ? '생존' : '사망'}</td>
        `;

        resultBody.appendChild(tr);        
      })

    })
    .catch(error => {
      console.error('검색 오류: ', error)
    })
}