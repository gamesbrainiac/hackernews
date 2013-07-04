from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from views import *

urlpatterns = patterns(
    '',
    url(r'^$', csrf_exempt(AllStories.as_view())),
    url(r'^make-story/$', login_required(MakeStory.as_view())),
)
