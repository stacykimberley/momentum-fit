from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('book/<int:class_id>/', views.book_class, name='book_class'),  # Book now page
]
