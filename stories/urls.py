from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from views import *

urlpatterns = patterns(
    '',
    url(r'^ajax/$', Ajax.as_view()),
    url(r'^$', AllStories.as_view()),
    url(r'^make-story/$', login_required(MakeStory.as_view())),
)
