from rest_framework import serializers

from inventory_list.models import Item, Photo
from users.serializers import UserSerializer


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('item_id', 'created', 'data', 'inventory')
    item_id = serializers.IntegerField()
    created = serializers.IntegerField()
    data = serializers.CharField()


class LiteItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('item_id', 'created', 'name', 'description', 'belongs_to', 'photo_set')

    info_id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    created = serializers.IntegerField(required=False)
    description = serializers.CharField()
    photo_set = PhotoSerializer(many=True)


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('item_id', 'created', 'name', 'description', 'belongs_to', 'photo_set')

    info_id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    created = serializers.IntegerField(required=False)
    description = serializers.CharField()
    belongs_to = UserSerializer(many=True)
    photo_set = PhotoSerializer(many=True)
# class BuildingComplexSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BuildingComplex
#         fields = ('info_id', 'name', 'complex_type', 'buildings_set')
#
#     info_id = serializers.IntegerField(required=False)
#     name = serializers.CharField()
#     complex_type = serializers.CharField()
#     buildings_set = CustomBuildingsField()
#
#     def create(self, validated_data):
#         building_complex = BuildingComplex(
#             name=validated_data.pop('name'),
#             complex_type=validated_data.pop('complex_type'),
#         )
#         building_complex.save()
#         complex_buildings = validated_data.get('buildings_set')
#         if complex_buildings:
#             building_complex.buildings_set.add(*complex_buildings)
#         return building_complex
#
#     def update(self, building_complex, validated_data):
#         building_complex.name = validated_data.get('name')
#         building_complex.complex_type = validated_data.get('complex_type')
#         building_complex.save()
#         building_complex.buildings_set.set(
#             Buildings.objects.filter(
#                 info_id__in=[building.info_id for building in validated_data.get('buildings_set', {})]
#             )
#         )
#         return building_complex
#
#     def validate(self, validated_data):
#         if not validated_data.get('name'):
#             ValidationError('Відсутня назва комплексу')
#         if not validated_data.get('complex_type'):
#             ValidationError('Відсутній тип комплексу')
#         return validated_data