from django.conf.urls import patterns, include, url
from django.contrib import admin
import intouch.queryset_csv


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'export/', include(intouch.queryset_csv.urls))
)
