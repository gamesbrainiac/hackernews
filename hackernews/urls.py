from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Stories app
    url(r'^stories/', include('stories.urls')),
    # Admin app
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Admin docs
    url(r'^admin/', include(admin.site.urls)),
    # login area
    url(r'^login/$', login, {'template_name': 'auth/login.html', }),
    # Logout area
    url(r'logout/$', logout, {'next_page': '/stories/', }),
)