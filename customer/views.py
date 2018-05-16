from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from tablib import Dataset

# Create your views here.
def customer_list(request):
    return HttpResponse("<h1>hello world!</h1>")

@csrf_exempt
def customer_import(request):
    if request.method == 'POST':
        print("Enter Post")
        return HttpResponse("<h1>Test post import!</h1>")
    else:
        return HttpResponse("<h1>Test import!</h1>")
