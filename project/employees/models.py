from django.db import models

class Employees(models.Model):
    emp_id = models.CharField(max_length=20)
    emp_name = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)
    
    def __str__(self):
        return self.emp_name
    
