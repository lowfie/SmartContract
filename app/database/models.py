from tortoise.models import Model
from tortoise import fields


class Token(Model):
    id = fields.IntField(pk=True)
    unique_hash = fields.CharField(max_length=32, unique=True, null=True)
    tx_hash = fields.CharField(max_length=32, null=True)
    media_url = fields.TextField(null=True)
    owner = fields.BigIntField(null=True)
