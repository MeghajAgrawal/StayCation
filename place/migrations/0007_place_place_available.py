# Generated by Django 3.0.2 on 2020-03-17 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0006_auto_20200314_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='place_available',
            field=models.BooleanField(default=True),
        ),
    ]
