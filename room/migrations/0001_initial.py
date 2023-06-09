# Generated by Django 4.2.1 on 2023-05-30 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='roomRoomModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='roomMessageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roomMessageModel_messages', to='room.roomroommodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roomMessageModel_messages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
