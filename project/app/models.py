from django.db import models



# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=50)
    cls  = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
        
