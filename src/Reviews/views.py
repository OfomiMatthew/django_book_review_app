from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  print(request.headers)
  return HttpResponse('<h1>Welcome to BookRev</h1>')