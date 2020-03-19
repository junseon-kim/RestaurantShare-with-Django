from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Category
from django.urls import reverse
# Create your views here.


def index(request):
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(request, 'shareRes/index.html', content)


def restaurantDetail(request):
    return render(request, 'shareRes/restaurantDetail.html')


def restaurantCreate(request):
    return render(request, 'shareRes/restaurantCreate.html')


def categoryCreate(request):
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(request, 'shareRes/categoryCreate.html', content)


def Create_category(request):
    category_name = request.POST['categoryName']
    new_category = Category(category_name=category_name)
    new_category.save()
    return HttpResponseRedirect(reverse('index'))
    # return HttpResponse('여기서 Create_category를 구현할거야')
