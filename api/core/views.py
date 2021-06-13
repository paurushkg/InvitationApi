from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated

from . serializers import *


class RelativeView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = RelativeSerializer
    lookup_field = 'event_name'

    def get_queryset(self):
        event_name = self.kwargs['event_name']
        user = self.request.user
        event = Event.objects.get(name=event_name)
        qs = Relative.objects.filter(host=user, event=event)
        return qs

    def perform_create(self, serializer):
        event_name = self.kwargs['event_name']
        user = self.request.user
        event = Event.objects.get(name=event_name)
        serializer.save(host=user, event=event)


class EventView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = EventSerializer

    def get_queryset(self):
        user = self.request.user
        events = Event.objects.filter(host=user)
        return events

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(host=user)


class MiniEventView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = MiniEventSerializer
    queryset = MiniEvent.objects.all()
    lookup_field = 'event_name'

    def filter_queryset(self, queryset):
        event_name = self.kwargs['event_name']
        user = self.request.user
        event = Event.objects.get(host=user, name=event_name)
        qs = queryset.filter(event=event)
        return qs

    def perform_create(self, serializer):
        event_name = self.kwargs['event_name']
        user = self.request.user
        event = Event.objects.get(host=user, name=event_name)
        serializer.save(event=event)


class GroomView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = GroomSerializer
    queryset = Groom.objects.all()
    lookup_field = 'event_name'

    def filter_queryset(self, queryset):
        event_name = self.kwargs['event_name']
        user = self.request.user
        event = Event.objects.get(host=user, name=event_name)
        qs = queryset.get(envent=event)
        return qs

    def perform_create(self, serializer):
        event_name = self.kwargs['event_name']
        user = self.request.user
        event = Event.objects.get(host=user, name=event_name)
        serializer.save(event=event)


class BrideView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = BrideSerializer
    queryset = Bride.objects.all()
    lookup_field = 'event_name'

    def filter_queryset(self, queryset):
        event_name = self.kwargs['event_name']
        user = self.request.user
        event = Event.objects.get(host=user, name=event_name)
        qs = queryset.get(envent=event)
        return qs

    def perform_create(self, serializer):
        event_name = self.kwargs['event_name']
        user = self.request.user
        event = Event.objects.get(host=user, name=event_name)
        serializer.save(event=event)
