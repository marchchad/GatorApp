from django.conf.urls import patterns, include, url

handler404 = 'jobs.views.FileNotFound'

urlpatterns = [
    url(r'^', include('jobs.urls'))
]