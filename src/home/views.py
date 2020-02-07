from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from meals.models import Meals, Category
from blog.models import Post
from aboutus.models import Why_Choose_Us


def home(request):
    meals = Meals.objects.all()
    context = {
        'meals': meals,
        'categories': Category.objects.all(),
        'meal_list': Meals.objects.all(),
        'posts': Post.objects.all(),
        'latest_post': Post.objects.last(),
        'whey_choose_us': Why_Choose_Us.objects.all()
    }
    return render(request, 'home/index.html', context)
