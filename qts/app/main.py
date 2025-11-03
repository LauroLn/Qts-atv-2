"""Main FastAPI application."""

from fastapi import FastAPI, HTTPException, status
from contextlib import asynccontextmanager
from app.api_client import ExternalServiceClient
from app.schemas import DataItemCreate, DataItemResponse
from typing import List

external_client = ExternalServiceClient()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup and shutdown events."""
    # Startup
    yield
    # Shutdown
    external_client.close()


app = FastAPI(
    title="FastAPI CI Sample",
    description="FastAPI project with CI/CD integration",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to FastAPI CI Sample"}


@app.get("/data", response_model=List[DataItemResponse])
async def get_all_data():
    """Fetch all data from external API."""
    try:
        data = await external_client.get_all_posts()
        return data
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Failed to fetch data from external API: {str(e)}",
        )


@app.get("/data/{data_id}", response_model=DataItemResponse)
async def get_data_by_id(data_id: int):
    """Fetch a single data item by ID from external API."""
    try:
        data = await external_client.get_post_by_id(data_id)
        if data is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Data item with id {data_id} not found",
            )
        return data
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Failed to fetch data from external API: {str(e)}",
        )


@app.post("/data", response_model=DataItemResponse, status_code=status.HTTP_201_CREATED)
async def create_data(data: DataItemCreate):
    """Create a new data item (simulated locally)."""
    try:
        new_data = await external_client.create_post(data.model_dump())
        return new_data
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Failed to create data: {str(e)}",
        )
