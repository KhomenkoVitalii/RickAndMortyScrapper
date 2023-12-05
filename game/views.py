import random
from django.http import JsonResponse
from django.contrib.auth import get_user_model, login, logout
from scrapper.models import Character
from scrapper.serializer import CharacterSerializer
from game.models import UserCard
from game.mixins import LikeModelMixin
from game.serializers import UserCardSerializer, UserLoginSerializer, UserRegisterSerializer, UserSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework import status, permissions

User = get_user_model()


class HomeView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        items = list(Character.objects.all())

        random_characters = random.sample(items, 4)

        serialized_characters = CharacterSerializer(
            random_characters, many=True).data

        for character in serialized_characters:
            character['image'] = request.build_absolute_uri(character['image'])

        return JsonResponse({'characters': serialized_characters})


class UserRegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        # TODO: ADD CUSTOM DATA VALIDATORS
        # clean_data = custom_validation(request.data)
        clean_data = request.data
        serializer = UserRegisterSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            if user:
                return Response(user, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = [SessionAuthentication,]

    def post(self, request, *args, **kwargs):
        data = request.data
        # TODO: ADD CUSTOM DATA VALIDATORS
        # assert validate_data(data)
        # assert validate_password(data)
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)


class UserLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, ]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            pass
        return Response({"message": "not implemented!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserCardView(ModelViewSet, LikeModelMixin):
    queryset = UserCard.objects.all()
    serializer_class = UserCardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        """
        Get all user cards for the authorized user.
        """
        user_cards = UserCard.objects.filter(user_id=self.request.user)
        serializer = UserCardSerializer(user_cards, many=True)
        return Response(serializer.data)

    def get_cards_of_chosen_user(self, request, user_id):
        # Filter user cards for the specified user ID
        chosen_cards = UserCard.objects.filter(user_id=user_id)
        serializer = UserCardSerializer(chosen_cards, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class AnotherUserCardsView(GenericViewSet):
    queryset = UserCard.objects.all()
    serializer_class = UserCardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = self.kwargs.get('user')

        if not user:
            return Response({"message": "user not provided!"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_obj = User.objects.get(username=user)
        except User.DoesNotExist:
            return Response({"message": "user not found!"}, status=status.HTTP_404_NOT_FOUND)

        chosen_cards = UserCard.objects.filter(user_id=user_obj.id)
        serializer = UserCardSerializer(chosen_cards, many=True)
        return Response(serializer.data)
