from django import forms
from .models import *
from django.contrib.auth.models import User	


class ClubForm(forms.ModelForm):
    CHOICES = (
         (
            (11, 'Brainverse Institute'),
            (12, 'Brainverse Collage'),
            (13, 'B4AU'),
        ))
    institution = forms.ChoiceField(choices=CHOICES)


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
