from django import forms
from .models import *
from django.contrib.auth.models import User	


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
