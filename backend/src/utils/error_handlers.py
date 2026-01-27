"""
Error handling utilities for the RAG Metrics Calculator API.
"""
from fastapi import HTTPException, status
from typing import Dict, Any, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class ValidationError(HTTPException):
    """Custom exception for validation errors."""
    
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "error": "VALIDATION_ERROR",
                "message": message,
                "details": details or {},
                "timestamp": datetime.utcnow().isoformat() + "Z"
            }
        )


class ProcessingError(HTTPException):
    """Custom exception for data processing errors."""
    
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={
                "error": "PROCESSING_ERROR",
                "message": message,
                "details": details or {},
                "timestamp": datetime.utcnow().isoformat() + "Z"
            }
        )


class FileTooLargeError(HTTPException):
    """Custom exception for file size limit exceeded."""
    
    def __init__(self, max_size_mb: int = 50) -> None:
        super().__init__(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail={
                "error": "FILE_TOO_LARGE",
                "message": f"File size exceeds maximum limit of {max_size_mb}MB",
                "timestamp": datetime.utcnow().isoformat() + "Z"
            }
        )


def create_error_response(
    error_code: str,
    message: str,
    details: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Create a standardized error response.
    
    Args:
        error_code: Error code identifier
        message: Human-readable error message
        details: Additional error details
        
    Returns:
        Standardized error response dictionary
    """
    return {
        "error": error_code,
        "message": message,
        "details": details or {},
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }


def log_error(error: Exception, context: Optional[Dict[str, Any]] = None) -> None:
    """
    Log error with context information.
    
    Args:
        error: Exception that occurred
        context: Additional context information
    """
    logger.error(
        f"Error occurred: {str(error)}",
        extra={"context": context or {}},
        exc_info=True
    )

# Made with Bob
