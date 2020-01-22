from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404,HttpResponseRedirect
from  club_management.forms import *

from django.http  import HttpResponse
import requests

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Club Managemnet')
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

    # logoutcode here

    # home page

@login_required(login_url='register')
def logout_view(request):
    logout(request)
    return redirect('login')

def index(request):
    current_user=request.user
    # if current_user.is_superuser==True:

    #     print(current_user.is_superuser,"Admiiiiin")

    #     return redirect(jamboAdmin_views.home)
    # else:

    return render(request, 'index.html')


@login_required(login_url='/accounts/login/')
def club_portal(request):
         current_user=request.user
  

         return render(request, 'club_portal.html')


@login_required(login_url='/accounts/login/')
def clubs(request):
    for detail in details:
        Institution = detail.get('instituion')
        Club_name = detail.get('club_name')
        
    return render(request, 'clubs.html', {'details': details})



@login_required(login_url='/accounts/login/')
def new_club(request):
    current_user = request.user
    if request.method == "POST":
        form = ClubForm(request.POST, request.FILES)
        if form.is_valid():
            club = form.save(commit=False)
            club.save()

            institution =form.CHOICES.get('institution')

            name = form.cleaned_data.get('club_name')
            email = form.cleaned_data.get('club_email')
            contact = form.cleaned_data.get('club_contact')

        


        return HttpResponseRedirect('/index')

    else:
        form = ClubForm()

    return render(request, 'register_club.html', {"form": form})




@login_required(login_url='/accounts/login/')
def new_official(request):
    current_user = request.user
    if request.method == "POST":
        form = OfficialForm(request.POST, request.FILES)
        if form.is_valid():
            official = form.save(commit=False)
            official.save()

            name = form.cleaned_data.get('official_name')
            position = form.cleaned_data.get('position')
            year = form.cleaned_data.get('leadership_year')

        


        return HttpResponseRedirect('/index')

    else:
        form = OfficialForm()

    return render(request, 'add_official.html', {"form": form})


@login_required(login_url='/accounts/login/')
def new_member(request):
    current_user = request.user
    if request.method == "POST":
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            member = form.save(commit=False)
            member.save()

            name = form.cleaned_data.get('member_name')
            academic_year = form.cleaned_data.get('academic_year')
            contact = form.cleaned_data.get('phone')

        


        return HttpResponseRedirect('/index')

    else:
        form = MemberForm()

    return render(request, 'add_member.html', {"form": form})
