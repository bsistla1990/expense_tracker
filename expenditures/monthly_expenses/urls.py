from django.conf.urls import url, include
from django.contrib import admin

from .views import *

urlpatterns = [
    #root urls
    url(r'^root$', RootListView.as_view()),
    url(r'^root/(?P<pk>\d+)', \
        RootDetailView.as_view(),name='read_root'),
    url(r'^root/create$', RootDetailView.as_view(), name='create_root'),
    url(r'^root/delete/(?P<pk>\d+)', \
        RootDetailView.as_view(), name='delete_root'),

    #family member urls
    url(r'^family/(?P<root_id>\d+)$', FamilyListView.as_view()),
    url(r'^family/(?P<root_id>\d+)/(?P<member_id>[a-f0-9]{8}-?[a-f0-9]{4}-?[a-f0-9]{4}-?[a-f0-9]{4}-?[a-f0-9]{12})', \
        FamilyDetailView.as_view(),name='read_family_member'),
    url(r'^family/(?P<root_id>\d+)/create$', FamilyDetailView.as_view(), name='create_family_member'),
    url(r'^family/delete/(?P<root_id>\d+)/(?P<member_id>[a-f0-9]{8}-?[a-f0-9]{4}-?[a-f0-9]{4}-?[a-f0-9]{4}-?[a-f0-9]{12})', \
        FamilyDetailView.as_view(), name='delete_root'),



]
