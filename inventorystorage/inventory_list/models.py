import time

from django.db import models


def get_return_time():
    # 1209600 is 2 weeks
    return time.time() + 1209600


class M2mInventoryToUser(models.Model):
    class Meta:
        db_table = 'm2m_inventory_to_user'

    item_id = models.AutoField(
        db_column='info_id',
        primary_key=True)

    inventory = models.ForeignKey('Item', on_delete=models.DO_NOTHING)
    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING)
    is_returned = models.BooleanField(default=False)
    return_time = models.BigIntegerField(default=0)
    has_to_be_returned = models.BigIntegerField(default=get_return_time)

    def __str__(self):
        return f'{self.inventory.name} у {self.user.last_name} {self.user.first_name}'


class Item(models.Model):
    class Meta:
        db_table = 'adminka_help'

    item_id = models.AutoField(
        primary_key=True)
    created = models.BigIntegerField(
        default=time.time
    )
    name = models.TextField()
    description = models.TextField()
    belongs_to = models.ManyToManyField(
        'users.User',
        through=M2mInventoryToUser,
        related_name='items'
    )

    def __str__(self):
        return f'{self.name} <id:{self.item_id}>'


class Photo(models.Model):
    item_id = models.AutoField(
        primary_key=True)
    created = models.BigIntegerField(
        default=time.time
    )
    data = models.TextField()
    inventory = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return f'Фотка номер {self.item_id} цінності {self.inventory}'
