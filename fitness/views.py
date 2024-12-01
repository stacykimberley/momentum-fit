from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from .models import FitnessClass, Booking
from .forms import BookingForm

def book_class(request, class_id):
    fitness_class = get_object_or_404(FitnessClass, id=class_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.fitness_class = fitness_class
            booking.save()

            # Update the number of booked spots
            fitness_class.booked += 1
            fitness_class.save()

            # Send email notification
            send_mail(
                'Booking Confirmation',
                f"Hi {booking.name},\n\nYou have successfully booked {fitness_class.name} "
                f"with {fitness_class.instructor.name} on {booking.date}. See you there!\n\nThanks,\nMomentum Fit",
                'your_email@example.com',  # Replace with your sender email
                [booking.email],
                fail_silently=False,
            )

            return redirect('home')  # Redirect to home page after booking
    else:
        form = BookingForm()

    return render(request, 'book_class.html', {
        'fitness_class': fitness_class,
        'form': form,
    })
