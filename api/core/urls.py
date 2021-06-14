from django.urls import path

from . views import *

urlpatterns = [
    path('event/', EventListCreateView.as_view()),
    path('update-event/<int:id>/', EventUpdateDeleteView.as_view()),

    path('relative/<str:event_name>/', RelativeListCreateView.as_view()),
    path('update-relative/<str:event_name>/<int:id>/', RelativeUpdateDeleteView.as_view()),

    path('mini_event/<str:event_name>/', MiniEventListCreateView.as_view()),
    path('update-mini-event/<str:event_name>/<int:id>/', MiniEventUpdateDeleteView.as_view()),

    path('groom/<str:event_name>/', GroomListCreateView.as_view()),
    path('update-groom/<str:event_name>/<int:id>/', GroomUpdateDeleteView.as_view()),

    path('bride/<str:event_name>/', BrideListCreateView.as_view()),
    path('update-bride/<str:event_name>/<int:id>/', BrideUpdateDeleteView.as_view()),

]
