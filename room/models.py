from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save

from djangochat_core.utils import slug_pre_save_receiver


class roomRoomModel(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.name


pre_save.connect(slug_pre_save_receiver, sender=roomRoomModel)

class roomMessageModel(models.Model):
    room = models.ForeignKey(roomRoomModel, related_name='roomMessageModel_room', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='roomMessageModel_user', on_delete=models.CASCADE)
    content = models.TextField()
    media_file = models.FileField(upload_to='room_media', blank=True)
    date_created = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.content

    @property
    def user_online_status(self):
        if self.user.accountsUserProfileModel_user.online:
            return 'Online'
        else:
            return 'Offline'


pre_save.connect(slug_pre_save_receiver, sender=roomMessageModel)

