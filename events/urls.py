from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.home, name='home'),
    path('events/<int:pk>/', views.event_detail, name='detail'),
    path('api/events/', views.api_events, name='api_events'),
    path('api/events/<int:pk>/register/', views.api_register, name='api_register'),
]
