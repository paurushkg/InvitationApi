from rest_framework import serializers

from . models import *
from accounts.serializers import *


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ['host']


class RelativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relative
        fields = '__all__'
        read_only_fields = ['event']


class MiniEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiniEvent
        fields = '__all__'
        read_only_fields = ['event']


class GroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groom
        fields = '__all__'
        read_only_fields = ['event']


class BrideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bride
        fields = '__all__'
        read_only_fields = ['event']


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'
        read_only_fields = ['relative', 'link_slug']
        depth = 2
