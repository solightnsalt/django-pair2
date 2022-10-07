from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
  path('', views.index, name='index'),
  path('board/', views.board, name='board'),
  path('create/', views.create, name='create'),
  path('<int:pk>/', views.detail, name="detail"),
  path('<int:pk>/delete/', views.delete, name="delete"),
  path('<int:pk>/update/', views.update, name="update"),
]