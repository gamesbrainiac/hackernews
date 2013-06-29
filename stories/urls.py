from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns(
    '',
    url(r'^ajax/$'),
    url(r'^make-story/$', MakeStory.as_view()),
    url(r'^$', AllStories.as_view()),
)
