"""Test fixtures and configuration."""

import pytest
from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch


@pytest.fixture
def test_client():
    """Create a test client for the FastAPI app."""
    client = TestClient(app)
    yield client


@pytest.fixture
def mock_api_client():
    """Mock the ExternalAPIClient."""
    # patch the instance name used in app.main (renamed to external_client)
    with patch("app.main.external_client") as mock:
        yield mock


@pytest.fixture
def sample_post_data():
    """Sample post data for testing."""
    return {
        "id": 1,
        "userId": 1,
        "title": "Test Post",
        "body": "This is a test post body",
    }


@pytest.fixture
def sample_posts_list():
    """Sample list of posts for testing."""
    return [
        {
            "id": 1,
            "userId": 1,
            "title": "Post 1",
            "body": "Body 1",
        },
        {
            "id": 2,
            "userId": 1,
            "title": "Post 2",
            "body": "Body 2",
        },
    ]


@pytest.fixture
def sample_create_data():
    """Sample data for creating a new post."""
    return {
        "title": "New Post",
        "body": "New post body",
        "userId": 1,
    }
