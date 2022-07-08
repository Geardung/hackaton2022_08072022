import peewee
import db


for z in [db.Users, db.Checks]:
    z.drop_table(cascade=True)
    

for z in [db.Checks, db.Users]:
    z.create_table()

