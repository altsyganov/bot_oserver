from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import UserRequest, Client, Bot
from .serializers import UserRequestSerializer, ClientSerializer


class UserRequestViewSet(ModelViewSet):

    queryset = UserRequest.objects.all()
    serializer_class = UserRequestSerializer


class ClientView(ListAPIView, CreateAPIView):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class BotView(APIView):

    def get(self, request):
        params = request.query_params
        if params:
            return Response(status=200, data=Bot.objects.get(ping_name=params['ping_name']).to_json())
        return Response(status=200, data=Bot.objects.get_json_payload())
