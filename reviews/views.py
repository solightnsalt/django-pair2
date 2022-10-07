from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

# Create your views here.

# index 페이지

def index(request):
  return render(request, 'reviews/index.html')


def board(request):
  context = {
    'reviews' : Review.objects.all().order_by('-created_at'),
  }
  return render(request, 'reviews/board.html', context)

def create(request):
  if request.method == "POST":
    review_form = ReviewForm(request.POST)
    if review_form.is_valid():
      review_form.save()
      return redirect("reviews:board")
  else:
    review_form = ReviewForm()
  context = {
    "review_form" : review_form
  }
  return render(request, 'reviews/create.html', context)

def update(request, pk):
  review = Review.objects.get(pk=pk)
  if request.method == "POST":
    review_form = ReviewForm(request.POST, instance=review)
    if review_form.is_valid():
      review_form.save()
      return redirect("reviews:board")
  else:
    review_form = ReviewForm(instance=review)
  context = {
    "review_form" : review_form,
    "num" : review.pk
  }
  return render(request, 'reviews/update.html', context)

def detail(request, pk):
  context = {
    "review": Review.objects.get(pk=pk),
  }
  return render(request, 'reviews/detail.html', context)

def delete(request, pk):
  review = Review.objects.get(pk=pk)
  review.delete()
  return redirect("reviews:board")