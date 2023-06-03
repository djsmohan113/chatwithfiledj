from django.urls import path
from .views import roomAdminGetUserMessagesGenericsView

urlpatterns = [
    path('api/room/<room_id>/', roomAdminGetUserMessagesGenericsView.as_view(), name='get_room_data'),
]
