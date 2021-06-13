from django.urls import path

from . views import *

urlpatterns = [
    path('event/', EventView.as_view()),
    path('relative/<str:event_name>', RelativeView.as_view()),
    path('mini_event/<str:event_name>/', MiniEventView.as_view()),
    path('groom/<str:event_name>/', GroomView.as_view()),
    path('bride/<str:event_name>/', BrideView.as_view()),
            ]
