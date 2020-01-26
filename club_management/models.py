from django.db import models
from django.contrib.auth.models import User
# from django import forms

# Create your models here.
# class Institution(models.Model):
#     STATUS_CHOICES = ((1, 'Brainverse Institute'),(2, 'Brainverse Technologies'))
#     # Institution = forms.ChoiceField(choices = STATUS_CHOICES) 
INSTITUTION_CHOICES = ( 
    ("1", "--Select--"), 

    ("2", "Brainverse Institute"), 
    ("3", "Brain verse college"), 
    ("4", "Brain Technical")
) 
  

class Club(models.Model):
    # institution= models.ForeignKey(Institution,on_delete=models.CASCADE,default=None)
    club_name = models.CharField(max_length=100)
    club_email = models.EmailField(max_length=50)
    club_contact =models.CharField(max_length=20)
    registered_on = models.DateField(auto_now_add=True)
    institution = models.CharField( max_length=200,choices = INSTITUTION_CHOICES, default=1  )


    def __str__(self):
        return self.club_name
    def save_club(self):
        self.save()
class Official(models.Model):
    club_name = models.ForeignKey(Club,on_delete=models.CASCADE,default=None)
    official_name = models.CharField( blank=False, max_length=50)
    position = models.CharField(blank=False, max_length=50)
    leadership_year = models.CharField(blank=False, max_length=50)
    phone = models.CharField(blank=False, max_length=50)
    school_or_faculty = models.CharField(blank=False, max_length=50)
    email = models.EmailField(max_length=50)
    course = models.CharField(max_length=200)

    def save_club_official(self):
        self.save()

class Member(models.Model):
    club = models.ForeignKey(Club,on_delete=models.CASCADE,default=None)
    member_name = models.CharField( blank=False, max_length=50)
    academic_year = models.CharField(blank=False, max_length=50)
    registration_number = models.CharField(blank=False, max_length=50)
    phone = models.CharField(blank=False, max_length=50)
    school_or_faculty = models.CharField(blank=False, max_length=50)
    email = models.EmailField(max_length=50)

    def save_member(self):
        self.save()
    

