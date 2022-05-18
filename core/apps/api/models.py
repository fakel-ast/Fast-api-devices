from tortoise.models import Model
from tortoise import fields


class Devices(Model):
    """Model for device"""
    dev_id = fields.CharField(max_length=200, index=True)
    dev_type = fields.CharField(max_length=120, index=True)


class Endpoint(Model):
    """Model for endpoint"""
    device = fields.ForeignKeyField('models.Devices', on_delete=fields.CASCADE)
    comment = fields.TextField(null=True)




