from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product
# Create your views here.


def calculate():
    x = 1
    y = 2
    return x


def say_hello(request):
    # Get Exception
    # product = Product.objects.get(pk=0).exists()
    # # None
    # exist = Product.objects.filter(pk=0).exists()

    # Filter
    # keyword=value
    fill = Product.objects.filter(price__gt=20)
    range = Product.objects.filter(price__range=(20, 30))
    coll = Product.objects.filter(collection__id__range=(1, 2, 3))

    return render(request, 't.html', {'name': 'Mosh'})
