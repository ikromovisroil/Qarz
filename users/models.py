from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=50,null=True,blank=True)
    tel = models.CharField(max_length=17,null=True,blank=True)
    tg = models.CharField(max_length=50,null=True,blank=True)
    
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # related_name ni o'zgartiring
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",  # related_name ni o'zgartiring
        blank=True
    )
    
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'user'