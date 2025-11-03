

import pytest
from unittest.mock import AsyncMock
from fastapi import status


class TestListDataEndpoint:
    """Testes para o endpoint GET /data."""

    @pytest.mark.asyncio
    async def test_list_data_success(
        self, test_client, mock_api_client, sample_posts_list
    ):
        """Recuperação bem-sucedida de todos os registros."""
        # Arrange
        mock_api_client.fetch_all_posts = AsyncMock(return_value=sample_posts_list)

        # Act
        response = test_client.get("/data")

        # Assert
        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.json(), list)
        assert len(response.json()) == 2
        assert response.json()[0]["title"] == "Post 1"

    @pytest.mark.asyncio
    async def test_list_data_api_failure(self, test_client, mock_api_client):
        """Falha quando a API externa está indisponível."""
        # Arrange
        mock_api_client.fetch_all_posts = AsyncMock(
            side_effect=Exception("API unavailable")
        )

        # Act
        response = test_client.get("/data")

        # Assert
        assert response.status_code == status.HTTP_503_SERVICE_UNAVAILABLE
        assert "Não foi possível obter" in response.json()["detail"]


class TestRetrieveDataEndpoint:
    """Testes para o endpoint GET /data/{id}."""

    @pytest.mark.asyncio
    async def test_retrieve_data_success(
        self, test_client, mock_api_client, sample_post_data
    ):
        """Recuperação bem-sucedida de um registro por ID."""
        # Arrange
        mock_api_client.fetch_post_by_id = AsyncMock(return_value=sample_post_data)

        # Act
        response = test_client.get("/data/1")

        # Assert
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["id"] == 1
        assert response.json()["title"] == "Test Post"

    @pytest.mark.asyncio
    async def test_retrieve_data_not_found(self, test_client, mock_api_client):
        """Tentativa de obter um registro inexistente retorna 404."""
        # Arrange
        mock_api_client.fetch_post_by_id = AsyncMock(return_value=None)

        # Act
        response = test_client.get("/data/999")

        # Assert
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "não encontrado" in response.json()["detail"].lower()

    @pytest.mark.asyncio
    async def test_retrieve_data_api_failure(self, test_client, mock_api_client):
        """Falha quando a API externa está indisponível ao buscar por ID."""
        # Arrange
        mock_api_client.fetch_post_by_id = AsyncMock(
            side_effect=Exception("API unavailable")
        )

        # Act
        response = test_client.get("/data/1")

        # Assert
        assert response.status_code == status.HTTP_503_SERVICE_UNAVAILABLE
        assert "Erro ao buscar dados" in response.json()["detail"]


class TestCreateDataEndpoint:
    """Testes para o endpoint POST /data."""

    @pytest.mark.asyncio
    async def test_create_data_success(
        self, test_client, mock_api_client, sample_create_data
    ):
        """Criação bem-sucedida de um novo registro."""
        # Arrange
        expected_response = {**sample_create_data, "id": 101}
        mock_api_client.create_new_post = AsyncMock(return_value=expected_response)

        # Act
        response = test_client.post("/data", json=sample_create_data)

        # Assert
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["id"] == 101
        assert response.json()["title"] == sample_create_data["title"]

    @pytest.mark.asyncio
    async def test_create_data_invalid_payload(self, test_client):
        """Validação do payload: dados inválidos retornam 422."""
        # Arrange
        invalid_data = {"invalid_field": "value"}

        # Act
        response = test_client.post("/data", json=invalid_data)

        # Assert
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    @pytest.mark.asyncio
    async def test_create_data_api_failure(
        self, test_client, mock_api_client, sample_create_data
    ):
        """Falha ao criar registro quando a API externa está indisponível."""
        # Arrange
        mock_api_client.create_new_post = AsyncMock(
            side_effect=Exception("API unavailable")
        )

        # Act
        response = test_client.post("/data", json=sample_create_data)

        # Assert
        assert response.status_code == status.HTTP_503_SERVICE_UNAVAILABLE
        assert "Falha ao criar novo registro" in response.json()["detail"]


class TestRootEndpoint:
    """Testes para o endpoint raiz (/) da aplicação."""

    def test_root_endpoint(self, test_client):
        """O endpoint raiz deve retornar a mensagem de boas-vindas."""
        # Act
        response = test_client.get("/")

        # Assert
        assert response.status_code == status.HTTP_200_OK
        assert "message" in response.json()
        assert "Welcome" in response.json()["message"]
