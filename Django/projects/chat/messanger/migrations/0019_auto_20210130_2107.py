# Generated by Django 3.1.5 on 2021-01-30 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20210130_2054'),
        ('messanger', '0018_friendlist'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FriendList',
            new_name='Friends',
        ),
        migrations.RenameField(
            model_name='friends',
            old_name='idfriendlist',
            new_name='idfriends',
        ),
    ]
