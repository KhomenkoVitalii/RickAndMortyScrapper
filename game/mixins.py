from game.models import UserCard
from django.contrib.contenttypes.models import ContentType
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status


class LikeModelMixin():
    @action(methods=['post'], detail=True, url_name="like")
    def like_action(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.is_liked:
            return Response({"status": "You already liked this card!"}, status=status.HTTP_400_BAD_REQUEST)

        obj.is_liked = True
        obj.save()
        return Response({"status": "liked"}, status=status.HTTP_201_CREATED)

    @action(methods=['post'], detail=True, url_name="unlike")
    def unlike_action(self, request, *args, **kwargs):
        obj = self.get_object()

        if not obj.is_liked:
            return Response({"status": "You haven't liked this card!"}, status=status.HTTP_400_BAD_REQUEST)

        obj.is_liked = False
        obj.save()
        return Response({"status": "unliked!"}, status=status.HTTP_202_ACCEPTED)
