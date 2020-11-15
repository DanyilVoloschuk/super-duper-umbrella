import time

from django.db import models


def get_return_time(self):
    # 1209600 is 2 weeks
    return time.time() + 1209600


class M2mInventoryToUser(models.Model):
    class Meta:
        db_table = 'm2m_geo_buildings_contractors'

    item_id = models.AutoField(
        db_column='info_id',
        primary_key=True)
    # do nothing cause we may need to get history of item
    inventory = models.ForeignKey('Item', on_delete=models.DO_NOTHING)
    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING)
    is_returned = models.BooleanField(default=False)
    return_time = models.BigIntegerField()
    has_to_be_returned = models.BigIntegerField(default=get_return_time)


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


class Photo(models.Model):
    item_id = models.AutoField(
        primary_key=True)
    created = models.BigIntegerField(
        default=time.time
    )
    data = models.TextField()
    inventory = models.ForeignKey(Item, on_delete=models.CASCADE)
