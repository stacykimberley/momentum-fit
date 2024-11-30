from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages  # Import messages framework
from .models import FitnessClass

def home(request):
    fitness_classes = FitnessClass.objects.all()
    return render(request, 'fitness/home.html', {'fitness_classes': fitness_classes})

def book_class(request, class_id):
    # Get the fitness class or 404 if it doesn't exist
    fitness_class = get_object_or_404(FitnessClass, id=class_id)

    # Check if the class is already full
    if fitness_class.is_full():
        # Add a message saying the class is full
        messages.error(request, f"Sorry, the class {fitness_class.name} is already full!")
        return render(request, 'fitness/class_full.html', {'fitness_class': fitness_class})

    # Otherwise, update the booking
    fitness_class.booked += 1
    fitness_class.save()

    # Add a success message for successful booking
    messages.success(request, f"You have successfully booked the class: {fitness_class.name}!")

    # Redirect to home after successful booking
    return redirect('home')  # Redirect back to the home page after booking
