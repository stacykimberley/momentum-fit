from django.contrib import admin
from .models import Exercise, Instructor, FitnessClass

# Register the models so they can be managed in the admin panel
admin.site.register(Exercise)
admin.site.register(Instructor)
admin.site.register(FitnessClass)