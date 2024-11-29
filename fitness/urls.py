from django.urls import path, include  # Make sure include is imported
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
