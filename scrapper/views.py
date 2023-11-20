from scrapper.models import Location, Character, Episode
from scrapper.serializer import LocationSerializer, CharacterSerializer, EpisodeSerializer
from rest_framework import status
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action

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


class SeasonEpisodeView(ReadOnlyModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        # Get the season number from the query parameters
        season_number = self.request.query_params.get('season')

        if season_number:
            # Log episodes for debugging
            episodes = Episode.objects.filter(
                episode__icontains=f'S{season_number}')
            print(season_number)

            # Continue with the rest of the code
            serializer = self.get_serializer(episodes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Provide general information about available seasons if no season number is provided
            seasons = Episode.objects.values_list(
                'episode', flat=True).order_by('episode').distinct()
            return Response({'episodes': seasons}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='count')
    def get_season_numbers(self, request, *args, **kwargs):
        # Get last episode
        episode = Episode.objects.last()

        # Check if episode is not None and episode number is in the expected format
        if episode and len(episode.episode) >= 3:
            # Get episode number
            number = episode.episode[1:3]
            return Response({'season_number': number}, status=status.HTTP_200_OK)
        else:
            # Handle the case where episode is None or not in the expected format
            return Response({'error': 'Invalid episode format'}, status=status.HTTP_400_BAD_REQUEST)
