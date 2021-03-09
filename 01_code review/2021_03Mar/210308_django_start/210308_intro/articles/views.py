from django.shortcuts import render
from django.http.response import HttpResponse
import random

def index(request):
    return HttpResponse('This is articles/ind3')
# Create your views here.

def mail(request):
    return HttpResponse("gmail.com")

def lotto(request):
    numbers = range(1, 46)
    lotto = random.sample(numbers,6)
    return HttpResponse(f'Pick: {sorted(lotto)}')