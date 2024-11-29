from django.shortcuts import render, redirect
from .models import FitnessClass
from django.contrib import messages

# Display available fitness classes
def home(request):
    fitness_classes = FitnessClass.objects.all()  # Fetch all fitness classes
    return render(request, 'fitness/home.html', {'fitness_classes': fitness_classes})

# Handle class booking
def book_class(request, class_id):
    fitness_class = FitnessClass.objects.get(id=class_id)

    # Check if the class is full
    if fitness_class.is_full():
        messages.error(request, "Sorry, this class is full.")
        return redirect('home')

    # Increment the booked count
    fitness_class.booked += 1
    fitness_class.save()

    # Show success message
    messages.success(request, f"You have successfully booked {fitness_class.name}!")
    return redirect('home')
