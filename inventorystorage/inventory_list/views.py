from rest_framework.response import Response
from rest_framework.views import APIView


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
        return Response(response)

    def post(self, request):
        response = {}
        data = request.data
        return Response(response)
