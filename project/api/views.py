# from django.shortcuts import render
# from django.http import JsonResponse
from app.models import student
from .serializers import studentSerializer, EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from employees.models import Employees


# Create your views here.
@api_view(['GET', 'POST'])
def studentViews(request):
    if request.method == 'GET':
        students = student.objects.all()
        serializers = studentSerializer(students, many= True)
        return Response(serializers.data, status=status.HTTP_200_OK)
 
    elif request.method == 'POST':
        serializer = studentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE']) 
def studentdetailViews(request, pk):
    try:
        std = student.objects.get(id=pk)
        print('std ============',std)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = studentSerializer(std)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer = studentSerializer(std, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        std.delete()
        return Response( status= status.HTTP_204_NO_CONTENT)
        
        
        
        
       
        
        
    
        
        
        
    
        
         
class Employee(APIView):
    
    def get(self, request):
        employees = Employees.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = EmployeeSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

            
    