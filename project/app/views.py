from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def students(request):
    students=[
        {'name': 'shashi','age':25,'city':'bengaluru'}
    ]
    return HttpResponse(students)