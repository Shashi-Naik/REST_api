from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse
from app.models import student
from .serializers import studentSerializer, EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from employees.models import Employees
from django.http import Http404
from rest_framework import mixins,generics,viewsets
from blogs.models import Blog,Comment
from blogs.serializers import BlogSerializer, CommentSerializer





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
        
        
        
        
       
        
        
    
        
        
        
# #===============class based ===========================================   
        
         
# class Employee(APIView):
    
#     def get(self, request):
#         employees = Employees.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self,request):
#         serializer = EmployeeSerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class EmployeeDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Employees.objects.get(pk=pk)
#         except Employees.DoesNotExist:
#             raise Http404
        
#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)    
    
#     def put(self,request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
#     def delete(self,request,pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
            
        
 #=============================******************=========================       
        
        
# class Employee(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    
#     queryset = Employees.objects.all()
#     serializer_class = EmployeeSerializer
    
#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)
    
''' # Mixins
class Employee(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)   
        
         
    # Mixins
class EmployeeDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    
    def get(self,request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)'''
        
    
    
'''    
# Generics 

class Employee(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer



# Generics 
class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'
'''
    
    
   
   
# class EmployeeViewset(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Employees.objects.all()
#         serializer = EmployeeSerializer(queryset, many=True)
#         return Response(serializer.data)
        
        
#     def create(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)
    
  
#     def retrive(self, request, pk = None):
#         Empl = get_object_or_404(Employees, pk=pk) 
#         serilizer = EmployeeSerializer(Empl)   
#         return Response(serilizer.data, status=status.HTTP_103_EARLY_HINTS)
            
        
class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer   
    
    
class BlogsView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer  
    

    

            
    