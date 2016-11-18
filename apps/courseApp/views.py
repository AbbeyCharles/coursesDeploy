from django.shortcuts import render, redirect
from .models import School

# Create your views here.
def index(request):
    school = School.objects.all()
    context = {
    'school' : school
    }
    return render(request, 'courseApp/index.html', context)

def classes(request):
    School.objects.create(name = request.POST['name'], description = request.POST['description'])
    return redirect('/')

def remove(request, id):
    course = School.objects.get(id=id)
    context = {
    'course' : course
    }
    return render (request, 'courseApp/remove.html', context)

def no(request):
    return redirect('/')

def yes(request, id):
    School.objects.filter(id=id).delete()
    return redirect('/')
