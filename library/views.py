from tokenize import Name
from django.shortcuts import render,redirect
from django.http import HttpResponse

from library.models import Book
from operation.views import display

def index(request):
    return render(request, 'library/index.html')


def add(request):
    name = request.POST['name']
    author = request.POST['author']
    edition = request.POST['edition']
    Book.objects.create(Name=name,Author=author,Edition=edition)
    return redirect(display)

def display(request):
    allbook = Book.objects.all()
    return render(request,'library/display.html',{'books':allbook})