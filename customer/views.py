from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def customer_list(request):
    return HttpResponse("<h1>hello world!</h1>")

def customer_import(request):
    if request.method == 'POST':
        return HttpResponse("<h1>Test post import!</h1>")
    else:
        return HttpResponse("<h1>Test import!</h1>")
