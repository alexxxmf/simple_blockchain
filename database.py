from peewee import *


db = SqliteDatabase('blockchain.db')


class BaseModel(Model):
    """
    This is the base model to use for the ORM
    """
    class Meta:
        database = db
