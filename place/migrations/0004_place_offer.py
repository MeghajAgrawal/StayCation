# Generated by Django 3.0.2 on 2020-03-08 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0003_auto_20200307_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='offer',
            field=models.BooleanField(default=False),
        ),
    ]
