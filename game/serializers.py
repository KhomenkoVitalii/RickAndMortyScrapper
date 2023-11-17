from rest_framework import serializers
from game.models import UserCard


class UserCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCard
        fields = '__all__'
