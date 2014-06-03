from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login',
      { 'template_name': 'accounts/login.html' }, name='login'),

    url(r'^logout/$', 'django.contrib.auth.views.logout', 
      { 'template_name': 'accounts/logout.html' }, name='logout'),

    url(r'^profile/$', TemplateView.as_view(
      template_name='accounts/profile.html'), name='profile'),
)
