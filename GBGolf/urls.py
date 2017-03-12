from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^manage/$', views.manage, name='GBGolfmanage'),
        url(r'^round/new/$', views.round_new, name='GBGolfround_new'),
        url(r'^course/new/$', views.course_new, name='GBGolfcourse_new'),
        url(r'^shots/new/$', views.shots_new, name='GBGolfshots_new'),
        url(r'^rounds/$', views.rounds, name='GBGolfrounds'),
        url(r'^delete_round/', views.delete_round, name='GBGolfdelete_round'),
        url(r'^handicap/$', views.handicap, name='GBGolfhandicap'),
        url(r'^sop/$', views.sop, name='GBGolfsop'),
        url(r'^$', views.home, name='GBGolfhome'),
    ]