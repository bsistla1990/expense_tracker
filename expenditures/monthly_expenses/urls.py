from django.conf.urls import url, include
from django.contrib import admin

from .views import IncomeView, FamilyView

urlpatterns = [
    url(r'income/', IncomeView.as_view()),
    url(r'family/', FamilyView.as_view())
]
