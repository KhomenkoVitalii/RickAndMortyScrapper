import pytest
from django.urls import reverse
from rest_framework import status
from .fixtures import user, authorized_client, character_card, usercard, usercard_liked


@pytest.mark.django_db
class TestUsercardActions:
    def test_action_like_usercard(self, usercard, authorized_client):
        url = reverse('usercard-like', kwargs={'pk': usercard.id})
        response = authorized_client.post(path=url)
        assert response.status_code == status.HTTP_201_CREATED

    def test_action_unlike_usercard(self, usercard_liked, authorized_client):
        url = reverse('usercard-unlike', kwargs={'pk': usercard_liked.id})
        response = authorized_client.post(path=url)
        assert response.status_code == status.HTTP_202_ACCEPTED

    def test_action_like_liked_usercard(self, usercard_liked, authorized_client):
        url = reverse('usercard-like', kwargs={'pk': usercard_liked.id})
        response = authorized_client.post(path=url)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_action_unlike_unliked_usercard(self, usercard, authorized_client):
        url = reverse('usercard-unlike', kwargs={'pk': usercard.id})
        response = authorized_client.post(path=url)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
