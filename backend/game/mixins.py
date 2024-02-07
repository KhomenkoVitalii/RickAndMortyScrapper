from game.models import UserCard, Like
from django.contrib.contenttypes.models import ContentType
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status


class LikeModelMixin():
    @action(methods=['post'], detail=True, url_name="like")
    def like_action(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.likes.filter(user=request.user).exists():
            return Response({"message": "You already liked this card!"}, status=status.HTTP_400_BAD_REQUEST)

        Like.objects.create(user=request.user, content_object=obj).save()
        return Response({"message": "liked"}, status=status.HTTP_201_CREATED)

    @action(methods=['post'], detail=True, url_name="unlike")
    def unlike_action(self, request, *args, **kwargs):
        obj = self.get_object()

        like = obj.likes.filter(user=request.user)

        if not like.exists():
            return Response({"message": "You haven't liked this card!"}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()
        return Response({"message": "unliked!"}, status=status.HTTP_202_ACCEPTED)
