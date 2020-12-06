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

    def __str__(self):
        return f'{self.last_name} {self.first_name} <id:{self.item_id}>'

    class Meta:
        verbose_name_plural = 'Користувачі'
        verbose_name = 'Користувач'
