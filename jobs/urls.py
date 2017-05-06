from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib import admin

from jobs import views

urlpatterns = patterns(
	'',
	# /
	url(r'^$', views.IndexView.as_view(), name='index'),
	# /job/5/
	url(r'^job/(?P<pk>\d+)/$', views.DetailView.as_view(), name='details'),
	# rest framework api
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    # user mgmt
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),
    # redirects any url that doesn't match back to home.
    # TODO: revisit this and possibly implement a 404 page instead.
    #url(r'^.*$', views.FileNotFound.raise404(), name='404')
    url(r'^.*$', RedirectView.as_view(url='/', permanent=False), name='index')
)