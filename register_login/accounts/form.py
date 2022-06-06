from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import Manager1,Employee1,Teja

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']
class ManagerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Manager1
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = '__all__'
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee1
        fields = '__all__'
class TejaForm(forms.ModelForm):
    class Meta:
        model=Teja
        fields='__all__'