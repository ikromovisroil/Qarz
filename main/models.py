from django.db import models
from users.models import User

class Employee(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=50)
    tel = models.CharField(max_length=20, null=True, blank=True)
    pazivnoy = models.CharField(max_length=10, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table = 'employee'


class Qarz(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    summa = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return str(self.summa)
    
    class Meta:
        db_table = 'qarz'
