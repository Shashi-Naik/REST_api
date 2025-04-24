from django.urls import path
from .import views

urlpatterns = [
    path('employee/', views.students, name='students'),
]
