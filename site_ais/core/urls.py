from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('ts', views.ts, name='ts'),
    path('projects', views.projects, name='projects'),
    path('animals', views.animals, name='animals'),
    path('lotus_meditation_project', views.lotus_meditation_project, name='lotus_meditation_project'),
]