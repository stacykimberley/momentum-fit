from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'fitness_class', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
