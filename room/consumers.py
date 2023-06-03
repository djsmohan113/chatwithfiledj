import base64
import json
import os
import uuid

from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.files.base import ContentFile

from accounts.models import accountsUserProfileModel
from .models import *
from .models import roomRoomModel, roomMessageModel


class roomChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        # print(text_data,'============================text')
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        media_file = text_data_json.get('media_file')

        print("Received message:", message)
        print("Received media_file:", media_file)

        modify_media_data= await self.save_message(message, media_file)
        # print(modify_media_data,'============================save message return')

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': self.scope['user'].username,
                'media_file': modify_media_data
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        media_file = event.get('media_file')

        # print("chat message is modify_media_data==================",media_file)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'media_file':media_file,
        }))

    @database_sync_to_async
    def save_message(self, message, media_file):
        room = roomRoomModel.objects.get(slug=self.room_name)
        user = User.objects.get(username=self.scope['user'].username)

        room_message = roomMessageModel.objects.create(
            room=room,
            user=user,
            content=message
        )
        file_object={}
        if media_file:
            media_data = media_file['data']  # Assuming 'data' contains the file data
            original_filename = media_file['name']
            extension = media_file['extension']
            unique_filename = f"{uuid.uuid4()}.{extension}"
            file_path = os.path.join('room_media', unique_filename)
            print(file_path, '============file path')
            content = base64.b64decode(media_data)
            media_file_obj = ContentFile(content, name=file_path)
            room_message.media_file.save(unique_filename, media_file_obj)

            file_object = {
                    'name': unique_filename,
                    'type': media_file['type'],
                    'extension': media_file['extension'],
                    'data': media_file['data'],
                }
            print("file object======",file_object)
            return file_object

    # @database_sync_to_async
    # def save_message(self, message, media_file):
    #     room = roomRoomModel.objects.get(slug=self.room_name)
    #     user = User.objects.get(username=self.scope['user'].username)
    #     print("Saving message:", message)
    #     print("Saving media_file:", media_file, type(media_file))
    #
    #     room_message = roomMessageModel.objects.create(
    #         room=room,
    #         user=user,
    #         content=message
    #     )
    #
    #     if media_file:
    #         media_data = media_file['data']  # Assuming 'data' contains the file data
    #         # Save the media file to a suitable location or process it as needed
    #         # For example, you can save it to a file on disk or upload it to a cloud storage service
    #         # Here, we will assume the media file is saved to a 'media' directory
    #
    #         # Generate a unique filename based on the original filename
    #         original_filename = media_file['name']
    #         extension = media_file['extension']
    #         unique_filename = f"{uuid.uuid4()}.{extension}"
    #
    #         # Decode and save the media file
    #         with open(os.path.join('media', unique_filename), 'wb') as file:
    #             file.write(base64.b64decode(media_data))
    #
    #         # Update the room message with the media file information
    #         room_message.media_file = os.path.join('media', unique_filename)
    #         # room_message.media_file = unique_filename
    #         room_message.save()
    #
    #     return room_message


#
# class roomChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         """
#         Called when the websocket is handshaking as part of the connection process.
#
#         It adds the channel to the corresponding room group and accepts the connection.
#         """
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name
#
#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )
#
#         await self.accept()
#         print(f"WebSocket connected to room: {self.room_name}", f'group name:{self.room_group_name}',
#               f'channel name{self.channel_name}')
#
#     async def disconnect(self, close_data):
#         """
#         Called when the WebSocket closes for any reason.
#
#         :param close_data: A string containing the close reason provided by the client.
#         """
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )
#         print(f"WebSocket disconnected from room: {self.room_name}")
#
#     async def receive(self, text_data):
#         """
#         Called when the server receives a WebSocket message from the client.
#         """
#         data = json.loads(text_data)
#         message = data['message']
#         username = data['username']
#         room = data['room']
#         media_file_data = data.get('media_file')
#
#         media_file = await self.save_media_file(media_file_data) if media_file_data else None
#         await self.save_message(username, room, message, media_file)
#
#         # Send message to room group
#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message,
#                 'username': username,
#                 'media_file': media_file.url if media_file else None
#             }
#         )
#
#     async def chat_message(self, event):
#         """
#         Called when a message is received from the room group.
#         """
#         message = event['message']
#         username = event['username']
#         media_file_url = event['media_file']
#
#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({
#             'message': message,
#             'username': username,
#             'media_file': media_file_url
#         }))
#
#     @sync_to_async
#     def save_message(self, username, room, message, media_file):
#         """
#         Save the message sent by the user to the database.
#         """
#         user = User.objects.get(username=username)
#         room = roomRoomModel.objects.get(slug=room)
#
#         room_message = roomMessageModel.objects.create(user=user, room=room, content=message, media_file=media_file)
#         print(f"Saved message to database: {message}")
#
#     @sync_to_async
#     def save_media_file(self, media_file_data):
#         """
#         Save the media file sent by the user to the server.
#         """
#         file_name = media_file_data['name']
#         file_content = media_file_data['content']
#         content_file = ContentFile(file_content)
#
#         media_file = roomMessageModel.media_file.field.generate_filename(self, file_name)
#         return roomMessageModel.media_file.field.storage.save(media_file, content_file, max_length=None)

# ==================================without media
#
# class roomChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         """
#         Called when the websocket is handshaking as part of the connection process.
#
#         It adds the channel to the corresponding room group and accepts the connection.
#         """
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name
#
#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )
#
#         await self.accept()
#         print(f"WebSocket connected to room: {self.room_name}", f'group name:{self.room_group_name}',
#               f'channel name{self.channel_name}')
#
#     async def disconnect(self, close_data):
#         print(self,'-----------self discoonect')
#         print(close_data,'===========close data')
#         """
#         Called when the WebSocket closes for any reason.
#
#         :param close_data: A string containing the close reason provided by the client.
#         """
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )
#         print(f"WebSocket disconnected from room: {self.room_name}")
#
#     async def receive(self, text_data):
#         """
#         Called when the server receives a WebSocket message from the client.
#         """
#         print(text_data, '--------------text data')
#         data = json.loads(text_data)
#         print(f"Received data from WebSocket: {data}")
#         message = data['message']
#         username = data['username']
#         room = data['room']
#
#         await self.save_message(username, room, message)
#
#         # Send message to room group
#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message,
#                 'username': username
#             }
#         )
#
#     async def chat_message(self, event):
#         """
#         Called when a message is received from the room group.
#         """
#         message = event['message']
#         username = event['username']
#
#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({
#             'message': message,
#             'username': username
#         }))
#         print(f"Sent message to WebSocket: {message}")
#
#     @sync_to_async
#     def save_message(self, username, room, message):
#         """
#         Save the message sent by the user to the database.
#         """
#         user = User.objects.get(username=username)
#         room = roomRoomModel.objects.get(slug=room)
#
#         roomMessageModel.objects.create(user=user, room=room, content=message)
#         print(f"Saved message to database: {message}")


class roomOnlineStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        print("User: status==", self.user)  # Print the user object for debugging
        await self.accept()
        print("Connection established==status")  # Print a message to indicate successful connection

        # Set the user's online status to True
        await self.update_online_status(True)

    async def disconnect(self, close_code):
        print("Disconnect status")  # Print a message to indicate disconnection
        # Set the user's online status to False
        await self.update_online_status(False)

    @database_sync_to_async
    def update_online_status(self, online):
        """
        @database_sync_to_async is specifically designed for use with Django ORM operations.
        If you need to perform other types of blocking I/O operations,
        such as making HTTP requests or interacting with external services, you would typically use
        different asynchronous libraries or utilities tailored for those specific operations.
        """
        profile = accountsUserProfileModel.objects.get(user=self.user)
        profile.online = online
        print("Profile status:", profile)  # Print the profile for debugging
        profile.save()

# class roomOnlineStatusConsumer(WebsocketConsumer):
#     def connect(self):
#         print("self=====================",self)
#         self.user = self.scope['user']
#         print("User: status==", self.user)  # Print the user object for debugging
#         self.accept()
#         print("Connection established==status")  # Print a message to indicate successful connection
#
#         # Set the user's online status to True
#         self.update_online_status(True)
#
#     def disconnect(self, close_code):
#         print("Disconnect status",close_code)  # Print a message to indicate disconnection
#         # Set the user's online status to False
#         self.update_online_status(False)
#
#     def update_online_status(self, online):
#         print("=================online or offline",online)
#         profile = accountsUserProfileModel.objects.get(user=self.user)
#         profile.online = online
#         print("Profile status:", profile)  # Print the profile for debugging
#         profile.save()
#
#


# class roomOnlineStatusConsumer(WebsocketConsumer):
#     def connect(self):
#         self.user = self.scope['user']
#         print("User: status==", self.user)  # Print the user object for debugging
#         self.accept()
#         print("Connection established==status")  # Print a message to indicate successful connection
#
#         # Set the user's online status to True
#         self.update_online_status(True)
#
#         # Notify the connected clients about the online status
#         self.broadcast_online_status(True)
#
#     def disconnect(self, close_code):
#         print("Disconnect status==============")  # Print a message to indicate disconnection
#         # Set the user's online status to False
#         self.update_online_status(False)
#
#         # Notify the connected clients about the online status
#         self.broadcast_online_status(False)
#
#     def update_online_status(self, online):
#         profile = accountsUserProfileModel.objects.get(user=self.user)
#         profile.online = online
#         print("Profile status=======:", profile)  # Print the profile for debugging
#         profile.save()
#
#     def broadcast_online_status(self, online):
#         # Get the online status of all users
#         online_users = accountsUserProfileModel.objects.filter(online=True).values_list('user__username', flat=True)
#         print("online users===========",online_users)
#         # Broadcast the online status to all connected clients
#         self.channel_layer.group_send(
#             'online_status',
#             {
#                 'type': 'online_status',
#                 'online': online,
#                 'online_users': list(online_users),
#             }
#         )
#
#     def online_status(self, event):
#         online = event['online']
#         online_users = event['online_users']
#         print("online =========",online,"online users==========",online_users)
#         # Send the online/offline status to the client
#         self.send(text_data=event['online'])
#
#
#
#
#
