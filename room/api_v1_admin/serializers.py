from rest_framework import serializers
from room.models import roomMessageModel


class roomMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = roomMessageModel
        fields = ['id', 'slug', 'room', 'user', 'content', 'media_file', 'date_created', 'slug', 'user_online_status', ]
        depth = 3
