
import random
from fastapi import FastAPI
import db, uvicorn
from fastapi.middleware.cors import CORSMiddleware

mmm = {
    "bakery": "5441" ,
    "gas": "5541" ,
    "clothes": "5691" ,
    "furniture": "5712" ,
    "things": "5732" ,
    "fastfood": "5814" ,
    "electronic": "5816" ,
    "drugs": "5912" ,
    "zoo": "5995" ,
    "auto": "7538" 
}


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)
    
@app.get("/sphere")
async def root(name=None, offset=0, sort=0):
    offset = int(offset)
    sort = int(sort)
    if (name is None) :
        return {"success": False, "message": "fuck you"}

    else:
        selection = db.Goods.select().where((db.Goods.mcc == mmm[name]))
        
        if sort > 0 : selection = db.Goods.select().where((db.Goods.mcc == mmm[name])).order_by(db.Goods.cost) 
        elif sort < 0: selection = db.Goods.select().where((db.Goods.mcc == mmm[name])).order_by(-db.Goods.cost) 
        
        
        if selection:
            return {"success": True, "result": [ {"name": str(x.name), "cost": str(x.cost), "mcc": str(x.mcc), "merchantname": str(x.merchantname)} for x in selection[offset:offset+100] ]}
        
        else: 
            return {"success": False, "message": "fuck you"}
       
       
@app.get("/chip_sphere")
async def lol(name=None,):
    if (name is None) :
        return {"success": False, "message": "fuck you"}

    else:
        lols = []
        selection = db.Goods.select().where((db.Goods.mcc == mmm[name]))
        while len(lols) < 5:
            a = random.choice(selection)
            if not a in lols: lols.append(a)
            
        if selection:
            return {"success": True, "result": [ [ {"name": str(x.name), "cost": str(x.cost), "mcc": str(x.mcc), 
                                                  "merchantname": str(x.merchantname)} for x in [db.Goods.select().where((db.Goods.name == lols[z].name))
                                                                                                     .order_by(db.Goods.cost)[0]]] for z in range(5)]}
        
        else: 
            return {"success": False, "message": "fuck you"}
        
@app.get("/get_shops")
async def zzz():
    z = db.Shops.select()
    if z: return {"success": True, "result": [{"name": x.name} for x in z]}
    else: return {"success": False, "message": "no shops"}
        
@app.get("/get_goods_by_shop")
async def fff(name=None):
    if name is None: return {"success": False, "message": "fck u"}
    else:
        z = db.Goods.select().where(db.Goods.merchantname == name)
        if z:
            return {"success": True, "result": [ {"name": str(x.name), "cost": str(x.cost), "mcc": str(x.mcc), 
                                                  "merchantname": str(x.merchantname)} for x in z]}

@app.get("/get_tovar_by_name")
async def fff(name=None):
    if name is None: return {"success": False, "message": "fck u"}
    else:
        z = db.Goods.select().where(db.Goods.name == name)
        if z:
            return {"success": True, "result": [ {"name": str(x.name), "cost": str(x.cost), "mcc": str(x.mcc), 
                                                  "merchantname": str(x.merchantname)} for x in z]}

@app.get("/get_rand_shops")
async def zzz(count=5):
    count = int(count)
    all = [a.name for a in db.Shops.select()]
    selected = []
    for i in range(count):
        selected.append(random.choice(all))
        all.pop(all.index(selected[-1]))
    return {"success": True, "result": selected}

if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, host='5.23.55.230', reload=True)