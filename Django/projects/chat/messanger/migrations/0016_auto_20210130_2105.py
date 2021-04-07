# Generated by Django 3.1.5 on 2021-01-30 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20210130_2054'),
        ('messanger', '0015_requeststofriendlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendlist',
            name='id',
        ),
        migrations.AddField(
            model_name='friendlist',
            name='friend1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='login.user'),
        ),
        migrations.AddField(
            model_name='friendlist',
            name='friend2',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='login.user'),
        ),
        migrations.AddField(
            model_name='friendlist',
            name='idfriendlist',
            field=models.AutoField(default=3, primary_key=True, serialize=False),
        ),
    ]
