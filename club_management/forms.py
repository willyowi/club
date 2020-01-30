from django import forms
from .models import *
from django.contrib.auth.models import User	
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser


class ClubForm(forms.ModelForm):

    class Meta:
        model = Club
        fields = '__all__'

class OfficialForm(forms.ModelForm):
    
    class Meta:
        model = Official
        fields = '__all__'

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model=CustomUser
        fields=('email',)


class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = ('email',)        
