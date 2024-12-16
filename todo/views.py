from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_list(request):
    return HttpResponse("Hello, list!")