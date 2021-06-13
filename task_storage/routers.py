from rest_framework.routers import DefaultRouter

from .api import UserRequestViewSet, ClientView

request_router = DefaultRouter()
request_router.register('requests', UserRequestViewSet, basename='request')

client_router = DefaultRouter()
client_router.register('clients', ClientView, basename='client')
