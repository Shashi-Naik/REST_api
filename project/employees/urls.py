from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.emp, name='emp'),
]
