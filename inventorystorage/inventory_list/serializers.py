from rest_framework import serializers

from inventory_list.models import Item, Photo
from users.models import User


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('item_id', 'created', 'data', 'inventory')

    item_id = serializers.IntegerField()
    created = serializers.IntegerField()
    data = serializers.CharField()


class LiteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('item_id', 'created', 'first_name', 'last_name', 'login', 'password', 'items')

    item_id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('item_id', 'created', 'name', 'description', 'belongs_to', 'photo_set')

    item_id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    created = serializers.IntegerField(required=False)
    description = serializers.CharField()
    belongs_to = LiteUserSerializer(many=True)
    photo_set = PhotoSerializer(many=True)


class LiteItemsSerializer(serializers.ModelSerializer):
    item_id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    description = serializers.CharField()
    photo_set = PhotoSerializer(many=True)

    class Meta:
        model = Item
        fields = ('item_id', 'created', 'name', 'description', 'belongs_to', 'photo_set')
