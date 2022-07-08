
from peewee import *
from playhouse.postgres_ext import PostgresqlExtDatabase

try:
    db = PostgresqlDatabase(
        database="hackaton",
        user="postgres",
        password="postgres",
        host='localhost',
        port=5432)

except:
    db = PostgresqlExtDatabase(
        database='hackaton',
        user='postgres',
        password="postgres",
        host='localhost', 
        port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Users(BaseModel):
    
    id = IntegerField(unique=True)
    
class Checks(BaseModel):
    
    UserId = TextField()
    CheckId = TextField()
    ProductName = TextField()
    ProductCost = TextField()
    MerchantName = TextField()
    MCC = TextField()