from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from . serializers import *


class RelativeListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = RelativeSerializer
    lookup_field = 'event_name'

    def get_event_object(self):
        event_name = self.kwargs['event_name']
        user = self.request.user
        try:
            event = Event.objects.get(host=user, name=event_name)
            return event
        except Event.DoesNotExist:
            raise NotFound({"detail": event_name + " " + "event not found"})

    def get_queryset(self):
        qs = Relative.objects.filter(event=self.get_event_object())
        return qs

    def perform_create(self, serializer):
        serializer.save(event=self.get_event_object())


class EventListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = EventSerializer

    def get_queryset(self):
        user = self.request.user
        events = Event.objects.filter(host=user)
        return events

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(host=user)


class MiniEventListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = MiniEventSerializer
    queryset = MiniEvent.objects.all()
    lookup_field = 'event_name'

    def get_event_object(self):
        event_name = self.kwargs['event_name']
        user = self.request.user
        try:
            event = Event.objects.get(host=user, name=event_name)
            return event
        except Event.DoesNotExist:
            raise NotFound({"detail": event_name + " " + "event not found"})

    def filter_queryset(self, queryset):
        qs = queryset.filter(event=self.get_event_object())
        return qs

    def perform_create(self, serializer):
        serializer.save(event=self.get_event_object())


class GroomListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = GroomSerializer
    queryset = Groom.objects.all()
    lookup_field = 'event_name'

    def get_event_object(self):
        event_name = self.kwargs['event_name']
        user = self.request.user
        try:
            event = Event.objects.get(host=user, name=event_name)
            return event
        except Event.DoesNotExist:
            raise NotFound({"detail": event_name + " " + "event not found"})

    def filter_queryset(self, queryset):
        qs = queryset.get(envent=self.get_event_object())
        return qs

    def perform_create(self, serializer):
        serializer.save(event=self.get_event_object())


class BrideListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = BrideSerializer
    queryset = Bride.objects.all()
    lookup_field = 'event_name'

    def get_event_object(self):
        event_name = self.kwargs['event_name']
        user = self.request.user
        try:
            event = Event.objects.get(host=user, name=event_name)
            return event
        except Event.DoesNotExist:
            raise NotFound({"detail": event_name + " " + "event not found"})

    def filter_queryset(self, queryset):
        qs = queryset.get(envent=self.get_event_object())
        return qs

    def perform_create(self, serializer):
        serializer.save(event=self.get_event_object())
