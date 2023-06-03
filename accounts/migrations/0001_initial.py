# Generated by Django 4.2.1 on 2023-05-31 12:14

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
            name='accountsUserProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('online', models.BooleanField(default=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='accountsUserProfileModel_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]