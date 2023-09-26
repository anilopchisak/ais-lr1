from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models

def index(request):
    return render(request=request, template_name='core/index.html')

def ts(request):
    return render(request=request, template_name='core/ts.html')

def projects(request):
    return render(request=request, template_name='core/projects.html')

def animals(request):
    animals = models.Animal.objects.all()
    context={'animals': animals}
    return render(request=request, template_name='core/animals.html', context=context)

def lotus_meditation_project(request):
    return render(request=request, template_name='core/lotus_meditation_project.html')



