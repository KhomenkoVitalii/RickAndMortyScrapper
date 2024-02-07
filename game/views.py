import random
from django.http import JsonResponse
from django.core.exceptions import ValidationError
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
from rest_framework.authtoken.models import Token


User = get_user_model()


class HomeView(APIView):
    """
    `HomeView` is a view in Django that handles the logic for the home page of the
    application. It is an API view that has method 'get' which returns 4 random characters for the main page
    (`permissions.AllowAny`).
    """
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
        serializer = UserRegisterSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = [SessionAuthentication,]

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.check_user(data)
            token, created = Token.objects.get_or_create(user=user)
            login(request, user)

            response_data = {
                "message": "Login successful!",
                "token": token.key,
                "user": {
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name
                }
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({'error': e.messages}, status=status.HTTP_401_UNAUTHORIZED)


class UserLogoutView(APIView):
    permission_classes = [permissions.AllowAny]

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
