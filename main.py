from core import ProcessInput
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/process")
async def process(batch: ProcessInput):
    print(batch)
    with open("urls.txt", "w+") as file:
        file.writelines([url + "\n" for url in batch.urls])


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
