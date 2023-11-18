import pytest
from scrapper.models import Character
from game.models import User, UserCard
from rest_framework.test import APIClient, force_authenticate


@pytest.fixture
def user():
    user = User.objects.create(username="test_user", password="test_user")
    return user


@pytest.fixture
def authorized_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client


@pytest.fixture
def character_card():
    character = Character.objects.create(
        name="Test Character", status="Alive", url="must_be_unique")
    return character


@pytest.fixture
def usercard(user, character_card):
    usercard = UserCard.objects.create(
        user_id=user, character_id=character_card)
    return usercard
