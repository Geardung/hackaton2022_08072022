import db


#for ind, buy in enumerate(db.Checks.select()):
#    z = db.Goods.select().where((db.Goods.merchantname == buy.MerchantName) &
#                                (db.Goods.name == buy.ProductName) &
#                                (db.Goods.mcc == buy.MCC)).first()
#    
#    if not z:
#        last = db.Goods.select().order_by(-db.Goods.id).first()
#        if last: last = last.id + 1
#        else: last = 1
#        try:
#            z = db.Goods.create(id = last, name = buy.ProductName,
#                                cost = int(buy.ProductCost), mcc = buy.MCC
#                                , merchantname = buy.MerchantName)
#            z.save()
#        except:
#            pass
#
#    z = db.Shops.select().where((db.Shops.name == buy.MerchantName)).first()
#    
#    if not z: 
#        l = db.Shops.create(name=buy.MerchantName)
#        l.save()
#    print(ind)

for buy in db.Goods.select():
    buy:db.Goods
    if buy.name == "Nan": 
        buy.delete_instance()
        buy.save()