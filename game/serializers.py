from rest_framework import serializers
from game.models import UserCard


class UserCardSerializer(serializers.ModelSerializer):
    user_id = serializers.StringRelatedField

    class Meta:
        model = UserCard
        fields = '__all__'
