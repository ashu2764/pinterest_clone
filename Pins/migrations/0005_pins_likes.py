# Generated by Django 4.1.1 on 2023-05-01 04:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Pins', '0004_alter_comments_comment_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='pins',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='Pin_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
