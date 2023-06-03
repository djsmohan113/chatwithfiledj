# Generated by Django 4.2.1 on 2023-06-01 04:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('room', '0002_alter_roommessagemodel_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roommessagemodel',
            options={'ordering': ['date_created']},
        ),
        migrations.AlterField(
            model_name='roommessagemodel',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roomMessageModel_room', to='room.roomroommodel'),
        ),
        migrations.AlterField(
            model_name='roommessagemodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roomMessageModel_user', to=settings.AUTH_USER_MODEL),
        ),
    ]