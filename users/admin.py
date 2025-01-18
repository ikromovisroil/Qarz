from django.contrib import admin
from .models import *

# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'first_name', 'tel', 'tg',)
    list_filter = ('is_active',)
    search_fields = ('name', 'last_name', 'first_name', 'tel', 'tg',)