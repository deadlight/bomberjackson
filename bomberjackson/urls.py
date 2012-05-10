from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),



    url(r'^$', 'posts.views.index', {'page_name': 'home'}, name='home'), #move to "news"
#posts
    url(r'^book/$', 'posts.views.selected', {'page_name': 'book'}, name='book'), #move to home
    url(r'^events/$', 'events.views.index', {'page_name': 'events'}, name='events'),
    url(r'^author/$', 'posts.views.selected', {'page_name': 'author'}, name='author'),
    url(r'^contact/$', 'posts.views.selected', {'page_name': 'contact'}, name='contact'),
    url(r'^buy/$', 'posts.views.selected', {'page_name': 'buy'}, name='buy'),

    url(r'^admin/', include(admin.site.urls)),
)
