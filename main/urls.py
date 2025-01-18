from django.urls import path
from .views import *

urlpatterns = [
    path('', profil, name='profil'),
    path('index/', index, name='index'),
    path('index/employee_edit/<int:pk>', employee_edit, name='employee_edit'),
    path('index/employee_delete/<int:pk>', employee_delete, name='employee_delete'),
    path('index/debt/<int:pk>', debt, name='debt'),
    path('index/debt/debt_edit/<int:pk>', debt_edit, name='debt_edit'),
    path('index/debt/debt_delete/<int:pk>', debt_delete, name='debt_delete'),
]