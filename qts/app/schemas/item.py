"""Schemas para o exemplo Item (create/update/response)."""

from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    description: str = None
    price: float
    tax: float = None


class ItemCreate(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


class ItemUpdate(BaseModel):
    name: str = None
    description: str = None
    price: float = None
    tax: float = None
