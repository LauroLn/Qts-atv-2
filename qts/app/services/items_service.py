from typing import List, Optional
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate


class ItemsService:
    """Serviço simples para manipulação de itens (em memória).

    Os métodos são assíncronos para se alinhar com as rotas que os
    consomem. O comportamento permanece in-memory e determinístico.
    """

    def __init__(self):
        self.items: List[Item] = []

    async def create_item(self, item_data: ItemCreate) -> Item:
        item = Item(id=len(self.items) + 1, **item_data.dict())
        self.items.append(item)
        return item

    async def get_item(self, item_id: int) -> Optional[Item]:
        for item in self.items:
            if item.id == item_id:
                return item
        return None

    async def update_item(self, item_id: int, item_data: ItemUpdate) -> Optional[Item]:
        item = await self.get_item(item_id)
        if item:
            for key, value in item_data.dict(exclude_unset=True).items():
                setattr(item, key, value)
            return item
        return None

    async def delete_item(self, item_id: int) -> bool:
        item = await self.get_item(item_id)
        if item:
            self.items.remove(item)
            return True
        return False

    async def list_items(self) -> List[Item]:
        return self.items
