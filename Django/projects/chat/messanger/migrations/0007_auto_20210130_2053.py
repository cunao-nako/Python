# Generated by Django 3.1.5 on 2021-01-30 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messanger', '0006_auto_20210129_0324'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='requeststofriendlist',
            name='id',
        ),
        migrations.AddField(
            model_name='requeststofriendlist',
            name='idrequeststofriendlist',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
