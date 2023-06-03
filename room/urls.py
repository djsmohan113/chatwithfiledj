from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('<int:id>/', views.room, name='room'),
    path('create-room/', views.create_room, name='create_room'),
    # path('delete-room/<int:id>/', views.delete_room, name='delete_room'),
    path('api/v1/admin/', include("room.api_v1_admin.urls")),
]

