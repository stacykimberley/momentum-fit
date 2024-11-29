from django.shortcuts import render
from .models import Exercise

def home(request):
    exercises = Exercise.objects.all()
    return render(request, 'fitness/home.html', {'exercises': exercises})

