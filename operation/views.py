from http.client import HTTPResponse
from django.shortcuts import render,redirect
from .models import Student
from django.http import HttpResponse

def index(request):
    return render(request, 'operation/index.html')

def add(request):
    name = request.POST['name']
    age = request.POST['age']
    Student.objects.create(Student_name=name,Student_age=age)
    return redirect(display)

def display(request):
    students = Student.objects.all()
    return render(request,'operation/display.html',{'student':students})

def delete(request,id):
    Student_delete = Student.objects.get(Student_id=id)
    Student_delete.delete()
    return redirect(display)

def edit(request,id):
    Student_edit = Student.objects.get(Student_id=id)
    if request.method == 'GET':
        return render(request,'operation/edit.html',{'student_edit':Student_edit})
    else:
        name = request.POST.get('name')
        age = request.POST.get('age')
        Student_edit.Student_name=name
        Student_edit.Student_age=age
        Student_edit.save()
        return redirect(display)
