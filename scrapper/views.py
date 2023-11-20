from django.shortcuts import render
from scrapper.models import Location, Character, Episode
from scrapper.serializer import LocationSerializer, CharacterSerializer, EpisodeSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny

# Create your views here.


class LocationView(ReadOnlyModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [AllowAny]
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['name', 'type']
    search_fields = ['name', 'type', 'dimension']


class CharacterView(ReadOnlyModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [AllowAny]
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['name', 'species']
    search_fields = ['name', 'species', 'type', 'gender']


class EpisodeView(ReadOnlyModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    permission_classes = [AllowAny]
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['name', 'episode']
    search_fields = ['name', 'episode']
