from fastapi import FastAPI, HTTPException

from practicerepo.models import Item, ItemCreate

app = FastAPI(title="PracticeRepo API")

# In-memory store
_items: dict[int, str] = {}
_next_id = 1


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/items", response_model=list[Item])
def list_items():
    return [Item(id=id, name=name) for id, name in _items.items()]


@app.post("/items", response_model=Item, status_code=201)
def create_item(payload: ItemCreate):
    global _next_id
    item = Item(id=_next_id, name=payload.name)
    _items[_next_id] = payload.name
    _next_id += 1
    return item


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="Item not found")
    return Item(id=item_id, name=_items[item_id])
