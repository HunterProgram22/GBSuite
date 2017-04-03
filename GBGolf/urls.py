from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import Manage, Round_new, Course_new, Shots_new, Rounds, \
    Rounds9, Delete_round, Handicap, Sop, Home, Putting, Range

urlpatterns = [
        url(r'^manage/$', login_required(Manage.as_view()), name='GBGolfmanage'),
        url(r'^round/new/$', login_required(Round_new.as_view()), name='GBGolfround_new'),
        url(r'^course/new/$', login_required(Course_new.as_view()), name='GBGolfcourse_new'),
        url(r'^shots/new/$', login_required(Shots_new.as_view()), name='GBGolfshots_new'),
        url(r'^rounds/$', login_required(Rounds.as_view()), name='GBGolfrounds'),
        url(r'^rounds9/$', login_required(Rounds9.as_view()), name='GBGolfrounds9'),
        url(r'^putt/$', login_required(Putting.as_view()), name='GBGolfpracticeputt'),
        url(r'^range/$', login_required(Range.as_view()), name='GBGolfpracticerange'),
        url(r'^delete_round/', login_required(Delete_round.as_view()), name='GBGolfdelete_round'),
        url(r'^handicap/$', login_required(Handicap.as_view()), name='GBGolfhandicap'),
        url(r'^sop/$', login_required(Sop.as_view()), name='GBGolfsop'),
        url(r'^$', login_required(Home.as_view()), name='GBGolfhome'),
    ]