from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items = [] #create an empty list

class Item(BaseModel):
    text:str = None
    is_done:bool = False

@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/items")
def create_item(new_items: list[Item]): #usage of class Item basemodel to print in such format
    items.extend(new_items)
    return items

@app.get("/list_items", response_model=list[Item]) #returntype from responsemodel confirms the expected structure, Removes sensitive or unnecessary fields automatically
def list_items(limit: int=10):
    return items[0:limit]

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id:int) -> Item:
    if item_id< len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail = f"Item{item_id} not found")



