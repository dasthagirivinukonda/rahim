from django.db import models
from django.urls import reverse
# Create your models here.
class Employee(models.Model):
    name= models.CharField(max_length=30)
    age= models.IntegerField()
    roolno= models.IntegerField()
    branch= models.CharField(max_length=30)
    def __str__(self):
        return self.name



    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

class Customer(models.Model):
    name=models.CharField(max_length=30)
    no=models.IntegerField()
    salary=models.FloatField()
    address=models.TextField()
    def __str__(self):
        return self.name
