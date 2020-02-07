from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Meals, Category


def meal_list(request):
    context = {
        'meal_list': Meals.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'Meals/list.html', context)


def meal_detail(request, slug):
    meal_detail = Meals.objects.get(slug=slug)
    context = {
        'meal_detail': meal_detail
    }
    return render(request, 'Meals/detail.html', context)
