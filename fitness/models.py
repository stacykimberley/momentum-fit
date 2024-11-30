from django.db import models

# Existing Exercise Model
class Exercise(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# New Instructor Model
class Instructor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Updated FitnessClass Model with price
class FitnessClass(models.Model):
    CLASS_CHOICES = [
        ('Pilates', 'Pilates'),
        ('Aqua Aerobics', 'Aqua Aerobics'),
        ('Cardio', 'Cardio'),
        ('Zumba', 'Zumba'),
    ]
    
    name = models.CharField(max_length=100, choices=CLASS_CHOICES)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    duration = models.DurationField()  # Duration in time format (e.g., timedelta)
    capacity = models.IntegerField(default=15)
    booked = models.IntegerField(default=0)  # Tracks number of people who have booked
    price = models.DecimalField(max_digits=5, decimal_places=2) 
    
    def __str__(self):
        return f"{self.name} with {self.instructor.name}"

    def is_full(self):
        """Check if the class has reached its capacity"""
        return self.booked >= self.capacity

    def available_spots(self):
        """Returns the number of spots available for the class"""
        return self.capacity - self.booked
