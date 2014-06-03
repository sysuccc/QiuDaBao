#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from qiudabao.forms import UserRegisterForm
from qiudabao.models import AccountInfo, Order

# Create your views here.

def user_register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if (form.is_valid()):
      uname = form.cleaned_data['username']
      psw   = form.cleaned_data['password']
      user  = User.objects.create_user(username=uname, password=psw)
      user.save()
      account = AccountInfo(user=user, balance=100)
      account.save()
      return HttpResponseRedirect(reverse('accounts:profile'))
  else: # GET
    form = UserRegisterForm()
  return render(request, 'qiudabao/register.html', { 'form': form })

def account_balance(request):
  accountinfo = AccountInfo.objects.get(user=request.user)
  context     = { 'accountinfo': accountinfo }
  return render(request, 'qiudabao/account_balance.html', context)

# All orders
class OrderListView(ListView):
  queryset            = Order.objects.filter(submiter=None)
  context_object_name = 'orders'
  template_name       = 'qiudabao/order_list.html'

# User offered orders
class UserOfferedOrders(ListView):
  context_object_name = 'orders'
  template_name       = 'qiudabao/user_offered_order_list.html'

  def get_queryset(self):
    orders = Order.objects.filter(offerer=self.request.user)
    return orders

# User submitted orders
class UserSubmittedOrders(ListView):
  context_object_name = 'orders'
  template_name       = 'qiudabao/user_submitted_order_list.html'

  def get_queryset(self):
    orders = Order.objects.filter(submiter=self.request.user)
    return orders

class OfferOrder(CreateView):
  model         = Order
  fields        = [ 'dish', 'description', 'place' ]
  template_name = 'qiudabao/offer_order.html'
  success_url   = reverse_lazy('qiudabao:order_list')

  def form_valid(self, form):
    # TODO: underflow case
    account = AccountInfo.objects.get(user=self.request.user)
    account.balance -= 1
    account.save()
    order = form.save(commit=False)
    order.offerer = self.request.user
    return super(OfferOrder, self).form_valid(form)

@require_POST
def submit_order(request):
  try:
    _id = request.POST.get('order_id')
    order = Order.objects.get(id=_id)
    order.submiter = request.user
    order.save()
  except: # FIXME, KeyError or objects get error
    raise Http404
  return HttpResponseRedirect(reverse('qiudabao:order_list'))

@require_POST
def confirm_order(request):
  try:
    _id = request.POST.get('order_id')
    order = Order.objects.get(id=_id)
    account = AccountInfo.objects.get(user=order.submiter)
    account.balance += 1
    account.save()
    order.delete()
  except Exception as ex:
    return HttpResponse(str(ex))
    raise Http404
  return HttpResponseRedirect(reverse('qiudabao:user_offered_order_list'))
