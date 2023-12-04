from django.forms import ValidationError
from rest_framework import serializers
from game.models import UserCard
from django.contrib.auth import get_user_model, authenticate

UserModel = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

    def create(self, clean_data):
        user_obj = UserModel.objects.create_user(email=clean_data['email'],
                                                 username=clean_data['username'],
                                                 password=clean_data['password'])
        user_obj.save()
        return user_obj


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    ##

    def check_user(self, clean_data):
        user = authenticate(
            email=clean_data['email'], password=clean_data['password'])
        if not user:
            raise ValidationError('user not found')
        return user


class UserSeriazer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('email', 'username')


class UserCardSerializer(serializers.ModelSerializer):
    user_id = serializers.StringRelatedField

    class Meta:
        model = UserCard
        fields = '__all__'
