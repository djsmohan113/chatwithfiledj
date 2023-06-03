from django import forms
from .models import roomRoomModel


class roomRoomForm(forms.ModelForm):
    class Meta:
        model = roomRoomModel
        fields = ['name']
