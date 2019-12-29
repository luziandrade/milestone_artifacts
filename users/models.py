from django.db import models
from django.contrib.auth.models import User as AuthorizedUser


class User(AuthorizedUser):
    class Meta:
        proxy = True
