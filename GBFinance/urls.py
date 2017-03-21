from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import Home, Manage, Balance, Balance_new, Income, Income_new, \
    Cash

urlpatterns = [
        url(r'^manage/$', login_required(Manage.as_view()), name='GBFinancemanage'),
        url(r'^balance/$', login_required(Balance.as_view()), name='GBFinancebalance'),
        url(r'^balance/new/$', login_required(Balance_new.as_view()), name='balance_new'),
        url(r'^income/$', login_required(Income.as_view()), name='GBFinanceincome'),
        url(r'^income/new/$', login_required(Income_new.as_view()), name='income_new'),
        url(r'^cash/$', login_required(Cash.as_view()), name='GBFinancecash'),
        url(r'^$', login_required(Home.as_view()), name='GBFinancehome'),
    ]