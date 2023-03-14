from tortoise import fields
from tortoise.models import Model


class Token(Model):
    id = fields.IntField(pk=True)
    unique_hash = fields.CharField(max_length=64, unique=True, null=True)
    tx_hash = fields.TextField(null=True)
    media_url = fields.TextField(null=True)
    owner = fields.TextField(null=True)
