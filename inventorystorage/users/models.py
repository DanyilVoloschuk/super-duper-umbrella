import time

from django.db import models


class User(models.Model):
    item_id = models.AutoField(
        primary_key=True)
    created = models.BigIntegerField(
        default=time.time
    )
    first_name = models.TextField()
    last_name = models.TextField()

    email = models.TextField()
    phone = models.TextField()

    login = models.TextField()
    password = models.TextField()
