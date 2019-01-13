from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    contact = forms.CharField(max_length=254, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','contact' )


# class LoginForm(AuthenticationForm):
#     username = forms.CharField(label='Username', max_length=30,
#                                widget=forms.TextInput(attrs={'class':'form-control', 'name': 'username'}))
#     password = forms.CharField(label='Password', max_length=30,
#                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
#
#     class Meta:
#         model = User
#         fields = ('username')
