from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'is_ogd_realtime_down.views.is_up', name='home'),
    url(r'^json$', 'is_ogd_realtime_down.views.is_up_json', name='is_up_json'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
