from django.urls import path
from .import views

urlpatterns = [
    path('std/', views.studentViews),
    path('std/<int:pk>/', views.studentdetailViews),
    
    path('employee/', views.Employee.as_view()),
    
     
]
