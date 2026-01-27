"""
Health check endpoint for API status monitoring.
"""
from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from typing import Literal

router = APIRouter()


class HealthResponse(BaseModel):
    """Health check response model."""
    status: Literal["healthy", "degraded", "unhealthy"]
    timestamp: str
    version: str = "1.0.0"


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """
    Health check endpoint.
    
    Returns:
        HealthResponse: Current health status of the API
    """
    return HealthResponse(
        status="healthy",
        timestamp=datetime.utcnow().isoformat() + "Z"
    )

# Made with Bob
