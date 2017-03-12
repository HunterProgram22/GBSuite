from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^manage/$', views.manage, name='GBFinancemanage'),
        url(r'^balance/$', views.balance, name='GBFinancebalance'),
        url(r'^balance/new/$', views.balance_new, name='balance_new'),
        url(r'^income/$', views.income, name='GBFinanceincome'),
        url(r'^income/new/$', views.income_new, name='income_new'),
        url(r'^cash/$', views.cash, name='GBFinancecash'),
        url(r'^cash/new/$', views.cash_new, name='cash_new'),
        url(r'^$', views.home, name='GBFinancehome'),
    ]