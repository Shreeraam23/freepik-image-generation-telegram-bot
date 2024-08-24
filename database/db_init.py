from tortoise import Tortoise, fields, run_async
from tortoise.models import Model

class User(Model):
    id = fields.BigIntField(pk=True)
    name = fields.CharField(max_length=255)
    authorized = fields.BooleanField(default=False)
    authorized_by = fields.BigIntField(null=True)

async def init_db():
    await Tortoise.init(
        db_url='sqlite://./database.db',
        modules={'models': ['database.models']},
    )
    await Tortoise.generate_schemas()

async def initilize():
    await init_db()

run_async(initilize())