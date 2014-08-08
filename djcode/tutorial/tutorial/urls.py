from django.conf.urls import *
from tutorial.views import hello, current_datetime, hours_ahead

urlpatterns = patterns('',
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
)