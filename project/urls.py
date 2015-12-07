from django.conf.urls import patterns, include, url
from django.contrib import admin
from main import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api_persons/$', views.APIPersonList.as_view()),
    url(r'^api_persons/(?P<pk>[0-9]+)/$', views.APIPersonDetail.as_view()),
    url(r'^person_list/$', views.PersonList.as_view()),
    url(r'^person_detail/(?P<pk>[0-9]+)/$', views.PersonDetail.as_view()),
    url(r'^person_update/(?P<pk>[0-9]+)/$', views.PersonUpdate.as_view()),
    url(r'^person_delete/(?P<pk>[0-9]+)/$', views.PersonDelete.as_view()),
    url(r'^person_create/$', views.PersonCreate.as_view()),
    url(r'^$', views.home),
)
