from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

urlpatterns = [

    path('', views.index_page, name='index'),
    path('contact', views.contact_page,name='contact'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
