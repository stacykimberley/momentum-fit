from django.urls import path
from . import views

urlpatterns = [
    # Add some basic routes to test the app
    path('', views.home, name='home'),
]
