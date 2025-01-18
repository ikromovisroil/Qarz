from .models import *
from django import forms
from django.contrib.auth.forms import UserChangeForm
from users.models import *


# profil form
class Userprofilform(UserChangeForm):
    class Meta:
        model = User
        fields = ('name','first_name','last_name','tel','tg',)

    def __init__(self,*args,**kwargs):
        super(Userprofilform,self).__init__(*args,**kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
            
class Employeeform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('full_name','tel','pazivnoy',)
        

class Qarzform(forms.ModelForm):
    class Meta:
        model = Qarz
        fields = ('summa',)