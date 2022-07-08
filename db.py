
from enum import unique
from peewee import *
from playhouse.postgres_ext import PostgresqlExtDatabase

try:
    db = PostgresqlDatabase(
        database="hackaton",
        user="postgres",
        password="postgres",
        host='5.23.55.230',
        port=5432)

except:
    db = PostgresqlExtDatabase(
        database='hackaton',
        user='postgres',
        password="postgres",
        host='5.23.55.230', 
        port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Users(BaseModel):
    
    id = IntegerField(unique = True)
    
class Goods(BaseModel):
    
    id = IntegerField(unique = True)

    name = TextField()
    
    cost = IntegerField()
    
    mcc = TextField()
    
    merchantname = TextField()
    

class Checks(BaseModel):
    
    id = TextField(unique=True, primary_key=True)
    
    UserId = TextField()
    
    CheckId = TextField()
    
    ProductName = TextField()
    
    ProductCost = TextField()
    
    MerchantName = TextField()
    
    MCC = TextField()
    