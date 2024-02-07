import pytest
from django.urls import reverse
from rest_framework import status
from game.tests.fixtures import user, authorized_client, character_card, usercard
from game.models import UserCard, AppUser
from game.serializers import UserCardSerializer


@pytest.mark.django_db
class TestUserCardApi:
    def test_list_authenticated_user(self, user, authorized_client, character_card, usercard):
        response = authorized_client.get(reverse('usercard-list'))

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]['user_id'] == usercard.user_id.id

    def test_list_another_user_cards(self, user, authorized_client, usercard):
        response = authorized_client.get(
            reverse('collection-list', kwargs={'user': user.username}))

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]['user_id'] == usercard.user_id.id

    def test_get_user_card(self, authorized_client, usercard):
        url = reverse('usercard-detail', args=[usercard.id])
        response = authorized_client.get(url)

        assert response.status_code == status.HTTP_200_OK

    def test_post_user_card(self, authorized_client, user, character_card):
        url = reverse('usercard-list')
        data = {'user_id': user.id, 'character_id': character_card.id}
        response = authorized_client.post(url, data)

        assert response.status_code == status.HTTP_201_CREATED

    def test_put_user_card(self, user, authorized_client, usercard, character_card):
        url = reverse('usercard-detail', args=[usercard.id])
        data = {'user_id': user.id,
                'character_id': character_card.id, 'is_liked': True}
        response = authorized_client.put(url, data)

        assert response.status_code == status.HTTP_200_OK

    def test_delete_user_card(self, authorized_client, usercard):
        url = reverse('usercard-detail', args=[usercard.id])
        response = authorized_client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
