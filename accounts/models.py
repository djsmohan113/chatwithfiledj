from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save, post_save, pre_delete

from djangochat_core.utils import slug_pre_save_receiver


# Create your models here.

class accountsUserProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="accountsUserProfileModel_user")
    online = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)

    def __str__(self):
        return self.user.username


pre_save.connect(slug_pre_save_receiver, sender=accountsUserProfileModel)
