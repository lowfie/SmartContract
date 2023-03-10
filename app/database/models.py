from tortoise.models import Model
from tortoise import fields


class Token(Model):
    id = fields.IntField(pk=True)
    unique_hash = fields.TextField(unique=True)
    tx_hash = fields.TextField()
    media_url = fields.TextField()
    owner = fields.BigIntField()
