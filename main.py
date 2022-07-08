
import random
from fastapi import FastAPI
import db, uvicorn

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

@app.get("/sphere")
async def root(name=None, offset=0):
    offset = int(offset)
    if (name is None) :
        return {"success": False, "message": "fuck you"}

    else:
        selection = db.Goods.select().where((db.Goods.mcc == mmm[name]))
        if selection:
            return {"success": True, "result": [ {"name": str(x.name), "cost": str(x.cost), "mcc": str(x.mcc), "merchantname": str(x.merchantname)} for x in selection[offset:offset+100] ]}
        
        else: 
            return {"success": False, "message": "fuck you"}
       
       
@app.get("/chip_sphere")
async def root(name=None,):
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
                                                  "merchantname": str(x.merchantname)} for x in db.Goods.select().where((db.Goods.name == lols[z].name))] for z in range(5)]}
        
        else: 
            return {"success": False, "message": "fuck you"}
        
        

if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, host='5.23.55.230', reload=True)