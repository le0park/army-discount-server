# Generated by Django 2.1.2 on 2019-11-20 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discountplace', '0004_auto_20191120_0425'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favoritelocation',
            old_name='longtitude',
            new_name='longitude',
        ),
    ]