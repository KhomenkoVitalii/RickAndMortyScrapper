import random
from django.http import JsonResponse, HttpResponseNotAllowed
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from scrapper.models import Character
from scrapper.serializer import CharacterSerializer
from game.models import UserCard
from game.serializers import UserCardSerializer
from game.forms import RegisterUserForm, LoginUserForm
from rest_framework.viewsets import ModelViewSet


def home(request):
    items = list(Character.objects.all())

    random_characters = random.sample(items, 4)

    return JsonResponse({'characters': CharacterSerializer(random_characters, many=True).data})


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


class UserCardView(ModelViewSet):
    queryset = UserCard.objects.all()
    serializer_class = UserCardSerializer
