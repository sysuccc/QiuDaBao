from django.conf.urls import patterns, include, url

from qiudabao.views import user_register, OrderListView
from qiudabao.views import account_balance
from qiudabao.views import UserOfferedOrders, UserSubmittedOrders
from qiudabao.views import OfferOrder, submit_order, confirm_order

urlpatterns = patterns('',

    url(r'^register/$', user_register, name='register'),

    url(r'^account_balance/$', account_balance, name='account_balance'),

    url(r'^order_list/$', OrderListView.as_view(), name='order_list'),

    url(r'^user_offered_order_list/$', UserOfferedOrders.as_view(),
      name='user_offered_order_list'),

    url(r'^user_submitted_order_list/$', UserSubmittedOrders.as_view(),
      name='user_submitted_order_list'),

    url(r'^offer_order/$', OfferOrder.as_view(), name='offer_order'),

    url(r'^submit_order/$', submit_order, name='submit_order'),

    url(r'^confirm_order/$', confirm_order, name='confirm_order'),
)
