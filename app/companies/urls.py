from django.urls import path

from . import views

urlpatterns = [
    path('', views.companies, name='company-list')
]
