from django.shortcuts import render, get_object_or_404, redirect
from .models import FitnessClass

def home(request):
    fitness_classes = FitnessClass.objects.all()
    return render(request, 'fitness/home.html', {'fitness_classes': fitness_classes})

def book_class(request, class_id):
    # Get the fitness class or 404 if it doesn't exist
    fitness_class = get_object_or_404(FitnessClass, id=class_id)

    # Check if the class is already full
    if fitness_class.is_full():
        # You can add a message saying the class is full
        return render(request, 'fitness/class_full.html', {'fitness_class': fitness_class})
    
    # Otherwise, update the booking
    fitness_class.booked += 1
    fitness_class.save()

    # Redirect to home or a success page
    return redirect('home')  # Redirect back to the home page after booking
