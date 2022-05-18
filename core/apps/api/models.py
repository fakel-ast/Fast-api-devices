from tortoise.models import Model
from tortoise import fields


class Male(Model):
    """Model for user male"""
    title = fields.CharField(max_length=16)





