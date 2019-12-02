"""
pages/urls.py
"""
from django.urls import path

from . import views

urlpatterns = [
    # Homepage
    path('', views.index_page, name='index_page'),
    path('contact', views.contact_page, name='contact_page'),

    # Gateway
    path('register', views.register_page, name='register_page'),
    path('register/success', views.register_success_page, name='register_success_page'),
    path('login', views.login_page, name='login_page'),
    path('logout', views.logout_page, name='logout_page'),

    # Dashboard
    path('dashboard', views.dashboard_page, name='dashboard_page'),

    # # Instruments
    path('instruments', views.i_list_page, name='i_list_page'),
    path('instrument/<int:id>', views.i_retrieve_page, name='i_retrieve_page'),
    path('instrument/<int:id>/update', views.i_update_page, name='i_update_page'),

    # Reports
    path('reports', views.report_list_page, name='report_list_page'),
    path('report/1', views.report_01_page, name='report_01_page'),

    # # Sensor
    # path('sensor/<int:id>', views.sensor_retrieve_page, name='sensor_retrieve_page'),

    # User Profile
    path('profile', views.profile_retrieve_page, name='profile_retrieve_page'),
    path('profile/update', views.profile_update_page, name='profile_update_page'),
]
