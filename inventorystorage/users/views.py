from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer
from users.models import User

class UsersListView(APIView):

    def get(self, request):
        response = {}
        users = User.objects.filter()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class Users(APIView):

    def get(self, request):
        response = {}
        data = request.GET
        return Response(response)

    def post(self, request):
        response = {}
        data = request.data
        return Response(response)

    def patch(self, request):
        response = {}
        data = request.data
        return Response(response)

    def put(self, request):
        response = {}
        data = request.data
        return Response(response)

    def delete(self, request, pk):
        return Response({})
