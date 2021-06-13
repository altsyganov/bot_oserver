from django.db import models

from .managers import BotManager


class TimeStampedModel(models.Model):

    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Bot(models.Model):

    name = models.CharField(max_length=100, blank=True)
    ping_name = models.CharField(max_length=100, blank=True)
    bug_responsible = models.CharField(max_length=70, blank=True)
    feat_responsible = models.CharField(max_length=70, blank=True)
    parent_chat = models.BigIntegerField(default=-591262988)

    objects = BotManager()

    def to_json(self):
        data = {
            'name': self.name,
            'ping_name': self.ping_name,
            'bug_responsible': self.bug_responsible,
            'feat_responsible': self.feat_responsible,
            'parent_chat_id': self.parent_chat
        }
        return data


class Client(models.Model):

    name = models.CharField(max_length=100)
    chat_id = models.BigIntegerField(primary_key=True)
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE, related_name='clients')


class UserRequest(TimeStampedModel):

    UNDEFINED = 'und'
    BUG = 'bug'
    FEATURE = 'feat'
    type_choices = (
        (UNDEFINED, 'Не разобрано'),
        (BUG, 'Ошибка'),
        (FEATURE, 'Добработка')
    )
    SELECTED = 'sel'
    REJECTED = 'rej'
    status_choices = (
        (UNDEFINED, 'Не разобрано'),
        (SELECTED, 'Принято'),
        (REJECTED, 'Отклонено')
    )

    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    body = models.TextField(blank=True)
    status = models.CharField(choices=status_choices, default=UNDEFINED, max_length=60)
    type = models.CharField(choices=type_choices, default=UNDEFINED, max_length=60)
    jira_link = models.URLField(blank=True)
    message_id = models.IntegerField(null=True, blank=True)

