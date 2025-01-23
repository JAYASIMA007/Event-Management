
from django.contrib import admin
from django.urls import path
from event_management_system_app import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.create_category, name='create_category'),
    path('categories/<int:category_id>/', views.category_events, name='category_events'),
    path('categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),
    path('events/create/', views.create_event, name='create_event'),
    path('events/update/<int:event_id>/', views.update_event, name='update_event'),
    path('events/delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('event-chart/', views.event_chart, name='event_chart'),
    path('', views.user_Login, name='login'),
    path('logout/', views.user_Logout, name='logout'),
    path('register/', views.user_Regi, name='registration'),
    path('profile/', views.user_Profile, name='profile'),
    path('address/', views.address, name='address'),
]
