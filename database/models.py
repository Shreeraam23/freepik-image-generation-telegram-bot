from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.BigIntField(pk=True)
    name = fields.CharField(max_length=255)
    authorized = fields.BooleanField(default=False)
    authorized_by = fields.BigIntField(null=True)