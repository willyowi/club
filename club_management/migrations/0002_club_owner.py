# Generated by Django 2.0.12 on 2020-01-30 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
