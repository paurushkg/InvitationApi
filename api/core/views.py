import datetime
import random
import json
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework import status, generics, views
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import NotFound, ValidationError
from . serializers import *

ALPHANUMERIC = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    'W', 'X', 'Y', 'Z'
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
    '-'
               ]


class Test(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = EventSerializer
    queryset = Event.objects.all()


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


class RelativeUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = RelativeSerializer
    lookup_field = 'id'

    def get_queryset(self):
        event_name = self.kwargs['event_name']
        user = self.request.user
        try:
            event = Event.objects.get(host=user, name=event_name)
        except Event.DoesNotExists:
            raise NotFound({"detail": event_name + " " + "event not found"})

        queryset = Relative.objects.filter(event=event)
        return queryset


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


class EventUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = EventSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        events = Event.objects.filter(host=user)
        return events


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


class MiniEventUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = MiniEventSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        event_name = self.kwargs['event_name']
        try:
            event = Event.objects.filter(host=user, name=event_name)
        except Event.DoesNotExists:
            raise NotFound({"detail": event_name + " " + "event not found"})
        qs = MiniEvent.objects.filter(event=event)
        return qs


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


class GroomUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = GroomSerializer
    lookup_field = 'id'

    def get_queryset(self):
        event_name = self.kwargs['event_name']
        user = self.request.user
        try:
            event = Event.objects.get(host=user, name=event_name)
        except Event.DoesNotExists:
            raise NotFound({"detail": event_name + " " + "event not found"})
        qs = Groom.objects.filter(event=event)
        return qs


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


class BrideUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = BrideSerializer
    lookup_field = 'id'

    def get_queryset(self):
        event_name = self.kwargs['event_name']
        user = self.request.user
        try:
            event = Event.objects.get(host=user, name=event_name)
        except Event.DoesNotExists:
            raise NotFound({"detail": event_name + " " + "event not found"})
        qs = Bride.objects.filter(event=event)
        return qs


class CardListCreateView(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated, ]
    serializer_class = CardSerializer

    def get_event_object(self):
        event_name = self.kwargs['event_name']
        user = self.request.user
        try:
            event = Event.objects.get(host=user, name=event_name)
            return event
        except Event.DoesNotExist:
            raise NotFound({"detail": event_name + " " + "event not found"})

    def get_relative_object(self):
        relative_id = self.kwargs['relative_id']
        relatives = Relative.objects.filter(event=self.get_event_object())
        try:
            relative = relatives.get(id=relative_id)
            return relative
        except Relative.DoesNotExist:
            raise NotFound({"detail": "relative with id" + " " + str(relative_id) + " " + "not found"})

    def get_queryset(self):
        qs = Card.objects.filter(relative=self.get_relative_object())
        return qs

    def perform_create(self, serializer):
        try:
            Card.objects.get(relative=self.get_relative_object())
        except Card.DoesNotExist:
            try:
                event = self.get_event_object()
                Groom.objects.get(event=event)
                Bride.objects.get(event=event)
            except:
                raise ValidationError({"detail": "groom or bride do not exist for this event"})

            slug = ''
            for i in range(10):
                index = random.randint(0, len(ALPHANUMERIC) - 1)
                slug += ALPHANUMERIC[index]
            serializer.save(relative=self.get_relative_object(), link_slug=slug)
        else:
            raise ValidationError({"detail": "card already exits"})


class CardDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = CardSerializer
    lookup_field = "link_slug"
    queryset = Card.objects.all()


class InviteView(views.APIView):

    permission_classes = [AllowAny, ]

    def get_relative_object(self, link_slug):
        card = Card.objects.get(link_slug=link_slug)
        return card.relative

    def get(self, request, link_slug):
        data = {}
        relative = self.get_relative_object(link_slug)
        event = relative.event
        host = relative.event.host
        mini_events = MiniEvent.objects.filter(event=event)
        groom = Groom.objects.get(event=event)
        bride = Bride.objects.get(event=event)

        data["to relative"] = model_to_dict(relative)
        data['host'] = model_to_dict(host, fields=["id", "first_name", "last_name", "email", "phone_number"])
        data['event'] = model_to_dict(event, fields=[field.name for field in event._meta.fields])
        data['groom'] = model_to_dict(groom)
        data['bride'] = model_to_dict(bride)
        data['mini_events'] = mini_events.values()
        print(data)
        return Response(data)
