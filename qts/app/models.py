"""Modelos de dados do aplicativo (simples e legíveis).

Esses modelos servem apenas para demonstração e conversão
entre formatos JSON/dicionário.
"""

from typing import Optional


class DataItem:
    """Representa um item de dado proveniente da API externa."""

    def __init__(
        self,
        id: int,
        userId: Optional[int] = None,
        title: Optional[str] = None,
        body: Optional[str] = None,
    ):
        self.id = id
        self.userId = userId
        self.title = title
        self.body = body

    def to_dict(self):
        """Converter o modelo para um dicionário simples."""
        return {
            "id": self.id,
            "userId": self.userId,
            "title": self.title,
            "body": self.body,
        }
