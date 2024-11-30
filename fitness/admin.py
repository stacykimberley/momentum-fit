from django.contrib import admin
from .models import Exercise, Instructor, FitnessClass

# Customizing the display of the FitnessClass model in the admin
class FitnessClassAdmin(admin.ModelAdmin):
    # Define which fields to display in the list view
    list_display = ['name', 'instructor', 'duration', 'capacity', 'booked', 'price']
    
    # Define which fields will appear in the detail view when adding or editing a FitnessClass
    fields = ['name', 'instructor', 'duration', 'capacity', 'booked', 'price']
    
    # Optionally, you can make certain fields read-only or add filtering options
    search_fields = ['name', 'instructor__name']
    list_filter = ['instructor', 'name']

# Register the models with the customized admin interface
admin.site.register(Exercise)
admin.site.register(Instructor)
admin.site.register(FitnessClass, FitnessClassAdmin)  # Register FitnessClass with the custom admin class
