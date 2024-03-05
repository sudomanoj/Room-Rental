from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from user.models import House, Room


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        
# class HouseForm(forms.ModelForm):
#     class Meta:
#         model = House
#         fields = ('area', 'floor', 'location', 'city', 'state', 'number', 'price', 'description', 'image')

class PasswordResetForm(PasswordResetForm):
    
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(attrs={"autofocus": True, 'class': 'form-control'}),
        required=True
    )
    class Meta:
        model = get_user_model
        fields = ['email']
        
class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={"autofocus": True, 'class': 'form-control'}),
        required=True
    )
    new_password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={"autofocus": True, 'class': 'form-control'}),
        required=True
    )
    class Meta:
        model = get_user_model()