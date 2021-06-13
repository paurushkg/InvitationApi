from django.urls import path

from . views import *

urlpatterns = [
    path('event/', EventListCreateView.as_view()),
    path('relative/<str:event_name>', RelativeListCreateView.as_view()),
    path('mini_event/<str:event_name>/', MiniEventListCreateView.as_view()),
    path('groom/<str:event_name>/', GroomListCreateView.as_view()),
    path('bride/<str:event_name>/', BrideListCreateView.as_view()),
            ]
