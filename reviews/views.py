from django.shortcuts import render
from .models import Review

# Create your views here.

# index 페이지

def index(request):
  return render(request, 'reviews/index.html')


def board(request):
  context = {
    'reviews' : Review.objects.all().order_by('-created_at'),
  }
  return render(request, 'reviews/board.html', context)