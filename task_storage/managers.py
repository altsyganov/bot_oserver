from django.db import models


class BotManager(models.Manager):

    def get_json_payload(self):
        payload = []
        for bot in self.all():
            payload.append(bot.to_json())
        return payload
