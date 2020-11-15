from rest_framework import serializers

from inventory_list.serializers import LiteItemsSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('item_id', 'created', 'first_name', 'last_name', 'login', 'password', 'items')
    item_id = serializers.IntegerField()
    created = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    login = serializers.CharField()
    password = serializers.CharField()
    items = LiteItemsSerializer()
