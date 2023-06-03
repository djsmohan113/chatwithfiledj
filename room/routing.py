from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/<str:room_name>/', consumers.roomChatConsumer.as_asgi()),
    path('ws/online/', consumers.roomOnlineStatusConsumer.as_asgi()),
]