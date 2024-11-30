from django.shortcuts import render, get_object_or_404
from .models import FitnessClass

def home(request):
    # Get all the fitness classes
    fitness_classes = FitnessClass.objects.all()
    return render(request, 'fitness/home.html', {'fitness_classes': fitness_classes})

def book_class(request, fitness_class_id):
    fitness_class = get_object_or_404(FitnessClass, id=fitness_class_id)
    
    # If there is space available in the class, increase the booked spots
    if not fitness_class.is_full():
        fitness_class.booked += 1
        fitness_class.save()
        message = "Your booking was successful!"
    else:
        message = "Sorry, this class is full."
    
    # Render a confirmation message on booking
    return render(request, 'fitness/book_class.html', {'fitness_class': fitness_class, 'message': message})
