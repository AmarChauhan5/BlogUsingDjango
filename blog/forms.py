from typing_extensions import ParamSpec

from django.db.models import fields
from . models import Post
from django.contrib.auth.forms import UserChangeForm, UserCreationForm,AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','style':'color: white;'}),label='Password(Again)')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','style':'color: white;'}),label='Password')
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets = {'username':forms.TextInput(attrs={'class':'form-control','style':'color: white;'}),
        'first_name':forms.TextInput(attrs={'class':'form-control','style':'color: white;'}),
        'last_name':forms.TextInput(attrs={'class':'form-control','style':'color: white;'}),
        'email':forms.EmailInput(attrs={'class':'form-control','style':'color: white;'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control','style':'color: white;'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','style':'color: white;'}))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {'disc':forms.Textarea(attrs={'class':'materialize-textarea','style':'color: white;'})}

class DashBoardChange(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']