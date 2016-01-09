from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'management.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
     url(r'^$','version1.views.show', name='show'),
     url(r'^shixi/$','version1.views.test', name='test'),
     url(r'^register/','version1.views.register', name='register' ),
     url(r'^login/','version1.views.login', name='login'),
     url(r'^submit/','version1.views.submit', name='submit'),
     url(r'^index/','version1.views.index', name='index'),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^logout/','version1.views.logout',name='logout'),
     url(r'^send/','version1.views.send',name='send'),
     url(r'^list/','version1.views.list',name='list'),
     url(r'^read/(.+)','version1.views.read',name='read'),
     url(r'^delete/(.+)/','version1.views.delete',name='delete'),
     url(r'^show/','version1.views.find',name = 'find'),
)
