from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'QiuDaBao.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('index.urls', namespace='index')),

    url(r'^accounts/', include('accounts.urls', namespace='accounts')),

    url(r'^qiudabao/', include('qiudabao.urls', namespace='qiudabao')),
)
