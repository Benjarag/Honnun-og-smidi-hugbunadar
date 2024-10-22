from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, Field
import requests
import uvicorn
import uuid

app = FastAPI(title="ItemService")

items = {}


class ItemCreateRequest(BaseModel):
    name: str
    email: str


class Item(BaseModel):
    id: str = Field(..., description="GUID of the item")
    name: str
    email: str


class SendEmailRequest(BaseModel):
    email: str
    message: str


@app.post("/items/", response_model=Item)
async def create_item(item: ItemCreateRequest):
    item_id = str(uuid.uuid4())
    item_data = Item(id=item_id, **item.model_dump())
    items[item_id] = item_data

    send_email_request = SendEmailRequest(
        email=item.email, message=f"Item {item.name} created"
    )

    requests.post(
        "http://localhost:8001/emails/", json=send_email_request.model_dump(), timeout=5
    )

    return item_data


@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: str):
    item = items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
