from django.shortcuts import render
from scrapper.models import Location, Character, Episode
from scrapper.serializer import LocationSerializer, CharacterSerializer, EpisodeSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet

# Create your views here.


class LocationView(ReadOnlyModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class CharacterView(ReadOnlyModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class EpisodeView(ReadOnlyModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
