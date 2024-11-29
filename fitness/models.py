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


# New FitnessClass Model
class FitnessClass(models.Model):
    CLASS_CHOICES = [
        ('Pilates', 'Pilates'),
        ('Aqua Aerobics', 'Aqua Aerobics'),
        ('Cardio', 'Cardio'),
        ('Zumba', 'Zumba'),
    ]
    
    name = models.CharField(max_length=100, choices=CLASS_CHOICES)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    duration = models.DurationField()  # 1 hour
    capacity = models.IntegerField(default=15)
    booked = models.IntegerField(default=0)  # Tracks number of people who have booked
    fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)  # Add fee field
    
    def __str__(self):
        return f"{self.name} with {self.instructor.name}"

    def is_full(self):
        return self.booked >= self.capacity
