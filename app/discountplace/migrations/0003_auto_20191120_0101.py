# Generated by Django 2.1.2 on 2019-11-20 01:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discountplace', '0002_auto_20191113_0524'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('user', 'place')},
        ),
    ]
