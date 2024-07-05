
from django.db import models
class Employee(models.Model):
    ename = models.CharField(max_length=50)
    esalary = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(max_length=100)
    edepartment = models.CharField(max_length=200)

    def __str__(self):
        return self.ename
