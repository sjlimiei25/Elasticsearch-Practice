from django.urls import path
from . import views

app_name = 'passengers'
urlpatterns = [
  path('', views.index),
  path('search/', views.search)
]