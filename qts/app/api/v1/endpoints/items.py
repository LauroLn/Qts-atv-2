from fastapi import APIRouter, HTTPException
from app.schemas.item import ItemCreate, ItemResponse
from app.services.items_service import ItemsService

router = APIRouter()
# instancia do serviço (nome curto para reduzir ruído nos handlers)
items_svc = ItemsService()


@router.post("/", response_model=ItemResponse)
async def create_item(item: ItemCreate):
    return await items_svc.create_item(item)


@router.get("/{item_id}", response_model=ItemResponse)
async def read_item(item_id: int):
    item = await items_svc.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.get("/", response_model=list[ItemResponse])
async def read_items(skip: int = 0, limit: int = 10):
    return await items_svc.list_items()
