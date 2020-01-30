from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    url(r'^$',views.index,name='Index'),
    path('club_portal/<str:club_name>/',views.club_portal,name='Index-Portal'),
    url(r'^new/club/$', views.new_club, name='new-club'),
    url(r'^new/member/$', views.new_member, name='new-member'),
    url(r'^new/official/$', views.new_official, name='new-official'),
    url(r'^clubs/$',views.clubs,name='clubs'),
    url(r'^officials/$',views.officials,name='officials'),
]