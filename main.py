
from fastapi import FastAPI
import db

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
async def root(name=None, user=None, offset=0):
    
    if (name is None) or (user is None):
        return {"success": False, "message": "fuck you"}

    else:
        
        pass