from django.db import models

class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=100)
    dept_location = models.CharField(max_length=200)

    def __str__(self):
        return self.dept_name

    class Meta:
        app_label = 'myapp'

class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=200)
    emp_salary = models.FloatField()
    emp_email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.emp_name
