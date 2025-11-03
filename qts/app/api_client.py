

import httpx
from typing import List, Optional


class JsonPlaceholderClient:
    """Cliente HTTP para comunicação com a API JSONPlaceholder.

    Mantive a assinatura dos métodos originais: fetch_all_posts,
    fetch_post_by_id, create_new_post e close.
    """

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        # cliente síncrono reutilizável (mantido para compatibilidade)
        self._client = httpx.Client(base_url=self.BASE_URL, timeout=10.0)

    async def fetch_all_posts(self) -> List[dict]:
        """Busca todos os posts disponíveis na API externa."""
        async with httpx.AsyncClient(base_url=self.BASE_URL, timeout=10.0) as client:
            response = await client.get("/posts")
            response.raise_for_status()
            return response.json()

    async def fetch_post_by_id(self, post_id: int) -> Optional[dict]:
        """Obtém um post específico pelo ID; retorna None se não for encontrado."""
        async with httpx.AsyncClient(base_url=self.BASE_URL, timeout=10.0) as client:
            response = await client.get(f"/posts/{post_id}")
            if response.status_code == 404:
                return None
            response.raise_for_status()
            return response.json()

    async def create_new_post(self, payload: dict) -> dict:
        """Cria um novo post (a API apenas simula a criação)."""
        async with httpx.AsyncClient(base_url=self.BASE_URL, timeout=10.0) as client:
            response = await client.post("/posts", json=payload)
            response.raise_for_status()
            return response.json()

    def close(self):
        """Fecha o cliente HTTP síncrono quando não for mais necessário."""
        self._client.close()
