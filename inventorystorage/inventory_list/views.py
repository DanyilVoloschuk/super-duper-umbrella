from rest_framework.response import Response
from rest_framework.views import APIView

from inventory_list.models import Item
from inventory_list.serializers import ItemsSerializer, LiteUserSerializer
from users.models import User


class SetItemToInventory(APIView):

    def post(self, request, pk):
        response = {}
        data = request.data
        login, password = data.values()
        print(data, pk)
        user = User.objects.filter(login=login, password=password).first()
        print(user)
        if not user:
            return Response({'errors': 'user is not found'})

        item = Item.objects.filter(item_id=pk).first()
        if not item:
            return Response({'errors': 'item is not found'})

        if item.belongs_to.count():
            return Response({'errors': 'item can`t be ordered'})

        user.items.add(item)
        response['message'] = 'Успішно додано!'
        response['user'] = LiteUserSerializer(user).data
        return Response(response)


class InventoryView(APIView):

    def get(self, request, pk):
        data = request.GET
        return Response({})

    def post(self, request):
        response = {}
        data = request.data
        return Response(response)

    def patch(self, request, pk):
        response = {}
        data = request.data
        return Response(response)

    def put(self, request, pk):
        response = {}
        data = request.data
        return Response(response)

    def delete(self, request, pk):
        return Response({})


class InventoryList(APIView):

    def get(self, request):
        response = {}
        data = request.GET
        items = Item.objects.filter()
        serializer = ItemsSerializer(items, many=True)
        response = serializer.data
        return Response(response)

    def post(self, request):
        response = {}
        data = request.data
        return Response(response)
