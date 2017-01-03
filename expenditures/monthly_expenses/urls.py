from django.conf.urls import url, include
from django.contrib import admin

from .views import *

urlpatterns = [

    #login/logout urls
    url(r'^login$', LoginView.as_view(),name='login_view'),
    url(r'^validate$', LoginValidationView.as_view(),name='login_validation_view'),
    url(r'^logout$', LogOutView.as_view(),name='logout_view'),

    #index url
    url(r'^$', HomeView.as_view(), name='home_view'),

    #root urls
    url(r'^root$', RootListView.as_view(), name='list_root'),
    url(r'^root/(?P<pk>\d+)', RootDetailView.as_view(),name='read_root'),
    url(r'^root/create$', RootDetailView.as_view(), name='create_root'),
    url(r'^root/delete/', RootDeleteView.as_view(), name='delete_root'),
    url(r'^root/modify/', RootUpdateView.as_view(), name='modify_root'),

    #family member urls
    url(r'^family/(?P<root_id>\d+)$', FamilyListView.as_view(), name='list_family'),
    url(r'^family/(?P<member_id>[a-f0-9]{8}-?[a-f0-9]{4}-?[a-f0-9]{4}-?[a-f0-9]{4}-?[a-f0-9]{12})', FamilyDetailView.as_view(),name='read_family_member'),
    url(r'^family/create$', FamilyDetailView.as_view(), name='create_family_member'),
    url(r'^family/delete/(?P<member_id>[a-f0-9]{8}-?[a-f0-9]{4}-?[a-f0-9]{4}-?[a-f0-9]{4}-?[a-f0-9]{12})', FamilyDetailView.as_view(), name='delete_root'),


    #income urls
    url(r'^income/(?P<root_id>\d+)$', IncomeListView.as_view(), name='list_income'),
    url(r'^income/filter$', IncomeFilterView.as_view(), name='filter_income'),
    url(r'^income/create$', IncomeDetailView.as_view(), name='create_income'),
    url(r'^income/(?P<member_id>[a-f0-9]{8}-?[a-f0-9]{4}-?[a-f0-9]{4}-?[a-f0-9]{4}-?[a-f0-9]{12})', IncomeDetailView.as_view(), name='read_income'),
    url(r'^income/delete/(?P<member_id>[a-f0-9]{8}-?[a-f0-9]{4}-?[a-f0-9]{4}-?[a-f0-9]{4}-?[a-f0-9]{12})', IncomeDetailView.as_view(), name='delete_income'),

    #expense urls
    url(r'^expense/(?P<root_id>\d+)$', ExpenseListView.as_view(), name='list_expense'),
    url(r'^expense/filter$', ExpenseFilterView.as_view(), name='filter_expense'),
    url(r'^expense/create$', ExpenseDetailView.as_view(), name='create_expense'),
    url(r'^expense/(?P<member_id>[a-f0-9]{8}-?[a-f0-9]{4}-?[a-f0-9]{4}-?[a-f0-9]{4}-?[a-f0-9]{12})', ExpenseDetailView.as_view(), name='read_expense'),
    url(r'^expense/delete/(?P<member_id>[a-f0-9]{8}-?[a-f0-9]{4}-?[a-f0-9]{4}-?[a-f0-9]{4}-?[a-f0-9]{12})', ExpenseDetailView.as_view(), name='delete_expense'),

]
