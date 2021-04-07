from django.test import TestCase

from login.models import User


class FriendList(User):
    username = User.objects.get(username)
