from django.urls import path, include

from . import api
from .routers import request_router

urlpatterns = [
    path('', include(request_router.urls)),
    path('clients/', api.ClientView.as_view(), name='clients'),
    path('bots/', api.BotView.as_view(), name='bots')
]
