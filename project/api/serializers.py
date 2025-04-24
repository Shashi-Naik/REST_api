from rest_framework import serializers
from app.models import student

from employees.models import Employees





class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'
        
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'
                