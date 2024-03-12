from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  name = request.GET.get('name') or "world"
  last = request.GET.get("last_name")
  print(name)
  return render(request,'base.html',{'name':name,'last':last})

def searchBooks(request):
  book = request.GET.get('book') 
  return render(request,'search.html',{'book':book})