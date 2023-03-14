from tortoise import fields
from tortoise.models import Model


class Token(Model):
    id = fields.IntField(pk=True)
    unique_hash = fields.CharField(max_length=256, unique=True, null=True)
    tx_hash = fields.CharField(max_length=256, null=True)
    media_url = fields.TextField(null=True)
    owner = fields.TextField(null=True)
