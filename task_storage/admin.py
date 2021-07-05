from django.contrib import admin

from .models import Bot, Client, UserRequest


@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):

    pass


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):

    pass


@admin.register(UserRequest)
class UserRequestAdmin(admin.ModelAdmin):

    pass
