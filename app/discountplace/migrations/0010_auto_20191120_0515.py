# Generated by Django 2.1.2 on 2019-11-20 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discountplace', '0009_auto_20191120_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placerequest',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='placerequest',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discountplace.Place'),
        ),
    ]
