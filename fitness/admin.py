from django.contrib import admin
from .models import Exercise, Instructor, FitnessClass

# Customizing the display of the FitnessClass model in the admin
class FitnessClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'instructor', 'duration', 'capacity', 'booked', 'price']  # Added 'price' here
    fields = ['name', 'instructor', 'duration', 'capacity', 'booked', 'price']
    search_fields = ['name', 'instructor__name']
    list_filter = ['instructor', 'name']

# Register the models with the customized admin interface
admin.site.register(Exercise)
admin.site.register(Instructor)
admin.site.register(FitnessClass, FitnessClassAdmin)  # Register FitnessClass with the custom admin class
