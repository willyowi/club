from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser



class ClubForm(forms.ModelForm):
    '''
    form to create a club
    '''
    class Meta:
        model = Club
        exclude=['owner']

class OfficialForm(forms.ModelForm):
    
    class Meta:
        model = Official
        exclude=['club_name']


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        exclude=['club']

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model=CustomUser
        fields=['email','password1','password2']        


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model=CustomUser
        fields=('email',)


class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = ('email',)        
