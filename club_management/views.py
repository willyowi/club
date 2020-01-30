from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404,HttpResponseRedirect
from  club_management.forms import *
from .models import *

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


@login_required(login_url='register')
def logout_view(request):
    logout(request)
    return redirect('login')

def index(request):
    current_user=request.user

    # fetch club associated with the curent logged in user
    club=Club.objects.filter(owner=current_user).first()

    return render(request, 'index.html',{'club':club})


@login_required(login_url='/accounts/login/')
def club_portal(request,club_name):
    '''
    view that redirects a person to their club
    params: pk of user the user,club name
    will need a custom decorator to prevent rogue access if you know a club name
    '''
    current_user=request.user
    # redirect user to their club

    return render(request, 'club_portal.html',{'club':club_name})


@login_required(login_url='/accounts/login/')
def clubs(request):
    '''
    view that renders all clubs
    '''

    details = Club.objects.all()

    return render(request,'clubs.html',{'details':details})
    # for detail in details:
    
    #     Institution = detail.get('instituion')
    #     Club_name = detail.get('club_name')
        
    # return render(request, 'clubs.html', )



@login_required(login_url='/accounts/login/')
def new_club(request):
    '''
    view to create a club
   
    '''
    current_user = request.user

    if request.method == "POST":
        form = ClubForm(request.POST, request.FILES)
        if form.is_valid():
            club = form.save(commit=False)
            club.owner=current_user
            club.save()

            institution =form.cleaned_data.get('institution')

            name = form.cleaned_data.get('club_name')
            email = form.cleaned_data.get('club_email')
            contact = form.cleaned_data.get('club_contact')

        # redirects to club view function to render clubs
        return HttpResponseRedirect('/clubs')

    else:
        form = ClubForm()
    
    return render(request, 'register_club.html', {"form": form})


@login_required(login_url='/accounts/login/')
def officials(request):
    '''
    view to render officials of a giveb club
    '''
    details = Official.objects.all()

    return render(request,'officials.html',{'details':details})


@login_required(login_url='/accounts/login/')
def new_official(request):
    '''
    view to add an official
    '''
    current_user = request.user
    # get club instance associated by the current_user
    club = Club.objects.filter(owner=current_user).first()

    if request.method == "POST":
        form = OfficialForm(request.POST, request.FILES)
        if form.is_valid():
            official = form.save(commit=False)
            # binding an official to a given club
            official.club_name = club
            official.save()

            name = form.cleaned_data.get('official_name')
            position = form.cleaned_data.get('position')
            year = form.cleaned_data.get('leadership_year')

        return HttpResponseRedirect('/officials')

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
