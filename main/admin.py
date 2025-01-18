from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('author','full_name','tel','pazivnoy',)
    list_filter = ('author','date',)
    search_fields = ('full_name','tel','pazivnoy',)


@admin.register(Qarz)
class QarzAdmin(admin.ModelAdmin):
    list_display = ('employee','summa','status','date',)
    list_filter = ('employee','status','date',)
    search_fields = ('employee__full_name','summa',)