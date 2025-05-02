from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employee', views.EmployeeViewset, basename='employee')
urlpatterns = [
    path('std/', views.studentViews),
    path('std/<int:pk>/', views.studentdetailViews),
    
    # path('employee/', views.Employee.as_view()),
    # path('employee/<int:pk>/', views.EmployeeDetail.as_view()),
    
    path('', include(router.urls)),
    
    path('Blogs/', views.BlogsView.as_view()),
    path('comments/', views.CommentView.as_view()),
         
    
     
]
