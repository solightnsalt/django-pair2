from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
  path('', views.index, name='index'),
  path('board/', views.board, name='board')
]