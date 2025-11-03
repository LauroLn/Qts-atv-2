"""Schemas Pydantic para validação de entrada/saída.

Pequenas reformulações de comentários para diferenciar do original.
"""

from pydantic import BaseModel, ConfigDict
from typing import Optional


class DataItemBase(BaseModel):
    """Esquema base para itens de dados."""

    title: str
    body: str
    userId: Optional[int] = None


class DataItemCreate(DataItemBase):
    """Esquema para criação de novo item de dado."""

    pass


class DataItemResponse(DataItemBase):
    """Resposta esperada para um item de dado."""

    id: int

    model_config = ConfigDict(from_attributes=True)
