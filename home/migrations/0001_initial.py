# Generated by Django 3.0.2 on 2020-02-15 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='images')),
                ('price', models.IntegerField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
