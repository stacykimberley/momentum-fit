from django.urls import path, include  # Make sure include is imported
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:fitness_class_id>/', views.book_class, name='book_class'),  # Booking page
]
