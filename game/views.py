import random
from django.http import JsonResponse, HttpResponseNotAllowed
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from scrapper.models import Character
from scrapper.serializer import CharacterSerializer
from game.models import UserCard, User
from game.mixins import LikeModelMixin
from game.serializers import UserCardSerializer
from game.forms import RegisterUserForm, LoginUserForm
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


def home(request):
    items = list(Character.objects.all())

    random_characters = random.sample(items, 4)

    serialized_characters = CharacterSerializer(
        random_characters, many=True).data

    for character in serialized_characters:
        character['image'] = request.build_absolute_uri(character['image'])

    return JsonResponse({'characters': serialized_characters})


def sign_in(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('/home/')

    if request.method == 'GET':
        form = LoginUserForm()
        return render(request, template_name='login.html', context={'login_form': form})

    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, "Sign in successfully!")
        return redirect('/home/')
    else:
        messages.error(request, "Incorrect data!")

    return HttpResponseNotAllowed(['GET', 'POST'])


def sign_up(request, *args, **kwargs):
    if request.method == "POST":
        # Handle form submission
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration success!")
            return redirect('/home/')
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    if request.user.is_authenticated:
        return redirect("/home/")
    form = RegisterUserForm()
    return render(request, template_name='registration.html', context={'register_form': form})


def logout_request(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('/home/')


class UserCardView(ModelViewSet, LikeModelMixin):
    queryset = UserCard.objects.all()
    serializer_class = UserCardSerializer
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]

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
