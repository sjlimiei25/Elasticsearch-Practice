from django.shortcuts import render
from django.http import JsonResponse

from .services.elastic_service import elastic_service as es

# Create your views here.
def index(req):
  return render(req, 'main.html')

def search(req):

  gender = req.GET.get('gender')
  survived = req.GET.get('survived')
  name = req.GET.get('name')
  size = req.GET.get('size')
  page = req.GET.get('page', 1)


  query_params = {
    'gender': gender,
    'survived': survived,
    'name': name,
    'size': size,
    'from': page
  }

  el_result = es.search_passenger(query_params)

  result=[]
  for hit in el_result['hits']['hits']:
    result.append(hit['_source'])

  return JsonResponse({'list':result
                       , 'total': el_result['hits']['total']['value']
                       , 'page': page})