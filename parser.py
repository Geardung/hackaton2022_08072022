import db

for buy in db.Checks.select():
    z = db.Goods.select().where((db.Goods.merchantname == buy.MerchantName) &
                                (db.Goods.name == buy.ProductName) &
                                (db.Goods.mcc == buy.MCC)).first()
    
    if not z:
        last = db.Goods.select().order_by(-db.Goods.id).first()
        if last: last = last.id + 1
        else: last = 1
        try:
            z = db.Goods.create(id = last, name = buy.ProductName,
                                cost = int(buy.ProductCost), mcc = buy.MCC
                                , merchantname = buy.MerchantName)
            z.save()
        except:
            pass