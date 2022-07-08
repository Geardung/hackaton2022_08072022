
import db


for z in [db.Users, db.Checks, db.Goods]:
    z.drop_table(cascade=True)
    

for z in [db.Goods, db.Checks, db.Users]:
    z.create_table()

