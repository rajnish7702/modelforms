from django.db import models

# Create your models here.

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=30)
    esal = models.FloatField()
    eaddr = models.TextField()

    def __str__(self) -> str:
        return 'Employee Object with eno: +str(self.no)'
