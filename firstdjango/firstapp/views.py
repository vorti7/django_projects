from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')
def lunch(request):
    menu_list = ["20층", "김카", "굶음"]
    pick= random.choice(menu_list)
    return render(request, 'lunch.html', {'lunch':pick})
def hello(request, name):
    return render(request,'hello.html', {'name':name})
def cube(request, num):
    multi = num**3
    return render(request, 'cube.html', {'multi': multi})