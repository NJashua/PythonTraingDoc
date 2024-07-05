from django.db import models

class Employee(models.Model):
    empid = models.IntegerField(primary_key=True)  # Explicitly define empid as primary key
    empname = models.CharField(max_length=50)
    empemail = models.CharField(max_length=200)
    empsal = models.FloatField()
    empadd = models.CharField(max_length=500)

    def __str__(self):
        return self.empname
