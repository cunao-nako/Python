from django.db import models
from django.utils import timezone

from login.models import User

class RequestsToFriendList(models.Model):
    idrequeststofriendlist = models.AutoField(primary_key=True)
    request_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    request_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')


class Friends(models.Model):
    idfriends = models.AutoField(primary_key=True)
    friend1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    friend2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')


class Chat(models.Model):
    idchat = models.AutoField(primary_key=True)
    friend1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    friend2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')


class Message(models.Model):
    idmessage = models.AutoField(primary_key=True)
    from_friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    to_friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    date_message = models.DateTimeField(default=timezone.now)
    idchat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='+')


class Text(models.Model):
    idtext = models.AutoField(primary_key=True)
    text = models.CharField(max_length=250)
    idmessage = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='+')
