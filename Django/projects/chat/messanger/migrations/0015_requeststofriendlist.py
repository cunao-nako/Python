# Generated by Django 3.1.5 on 2021-01-30 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20210130_2054'),
        ('messanger', '0014_delete_requeststofriendlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestsToFriendList',
            fields=[
                ('idrequeststofriendlist', models.AutoField(primary_key=True, serialize=False)),
                ('request_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='login.user')),
                ('request_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='login.user')),
            ],
        ),
    ]
