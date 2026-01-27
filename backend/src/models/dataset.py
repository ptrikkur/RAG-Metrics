"""
Pydantic models for dataset-related data structures.
"""
from pydantic import BaseModel, Field, field_validator
from typing import List, Dict, Any, Optional
from datetime import datetime


class ColumnMapping(BaseModel):
    """Column mapping for CSV data."""
    query: str = Field(..., description="Column name for query text")
    response: str = Field(..., description="Column name for generated responses")
    groundTruth: str = Field(..., alias="groundTruth", description="Column name for ground truth answers")
    metadata: Optional[Dict[str, str]] = Field(default=None, description="Additional column mappings")
    
    class Config:
        populate_by_name = True


class DataRow(BaseModel):
    """Single row of RAG evaluation data."""
    rowIndex: int = Field(..., alias="rowIndex", ge=1, description="Row number in CSV (1-based)")
    query: str = Field(..., min_length=1, max_length=10000, description="Input query/question")
    response: str = Field(..., min_length=1, max_length=10000, description="Generated response")
    groundTruth: str = Field(..., alias="groundTruth", min_length=1, max_length=10000, description="Correct answer")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Additional fields from CSV")
    
    class Config:
        populate_by_name = True


class ValidationStatus(BaseModel):
    """Validation status for uploaded CSV."""
    status: str = Field(..., description="Validation status: VALID or INVALID")
    errors: Optional[List[Dict[str, Any]]] = Field(default=None, description="List of validation errors")


class ValidationError(BaseModel):
    """Individual validation error."""
    code: str = Field(..., description="Error code")
    message: str = Field(..., description="Human-readable error message")
    severity: str = Field(..., description="ERROR or WARNING")
    rowIndex: Optional[int] = Field(default=None, alias="rowIndex", description="Row number where error occurred")
    columnName: Optional[str] = Field(default=None, alias="columnName", description="Column name where error occurred")
    
    class Config:
        populate_by_name = True


class DatasetMetadata(BaseModel):
    """Metadata about the uploaded dataset."""
    fileSize: int = Field(..., alias="fileSize", description="File size in bytes")
    encoding: str = Field(default="UTF-8", description="Character encoding")
    delimiter: str = Field(default=",", description="CSV delimiter")
    hasHeader: bool = Field(default=True, alias="hasHeader", description="Whether CSV has header row")
    columnCount: int = Field(..., alias="columnCount", ge=1, description="Number of columns")
    
    class Config:
        populate_by_name = True


class RAGDataset(BaseModel):
    """Complete RAG evaluation dataset."""
    id: str = Field(..., description="Unique identifier (UUID)")
    fileName: str = Field(..., alias="fileName", min_length=1, description="Original CSV filename")
    uploadTimestamp: str = Field(..., alias="uploadTimestamp", description="Upload timestamp (ISO-8601)")
    rowCount: int = Field(..., alias="rowCount", ge=1, le=10000, description="Number of data rows")
    columnMappings: ColumnMapping = Field(..., alias="columnMappings", description="Column name mappings")
    data: List[DataRow] = Field(..., description="Array of data rows")
    validationStatus: ValidationStatus = Field(..., alias="validationStatus", description="Validation result")
    metadata: DatasetMetadata = Field(..., description="Dataset metadata")
    
    @field_validator('data')
    @classmethod
    def validate_data_length(cls, v: List[DataRow], info: Any) -> List[DataRow]:
        """Validate that data length matches rowCount."""
        if 'rowCount' in info.data and len(v) != info.data['rowCount']:
            raise ValueError(f"Data length ({len(v)}) does not match rowCount ({info.data['rowCount']})")
        return v
    
    class Config:
        populate_by_name = True


class ValidationResponse(BaseModel):
    """Response from CSV validation endpoint."""
    valid: bool = Field(..., description="Whether the CSV is valid")
    rowCount: int = Field(..., alias="rowCount", description="Number of data rows")
    columns: List[str] = Field(..., description="List of column names")
    detectedMappings: Optional[ColumnMapping] = Field(default=None, alias="detectedMappings", description="Auto-detected mappings")
    preview: Optional[List[Dict[str, Any]]] = Field(default=None, description="First 10 rows preview")
    warnings: Optional[List[ValidationError]] = Field(default=None, description="Non-critical warnings")
    
    class Config:
        populate_by_name = True


class ValidationErrorResponse(BaseModel):
    """Response when CSV validation fails."""
    valid: bool = Field(default=False, description="Always false for error response")
    errors: List[ValidationError] = Field(..., description="List of validation errors")
    
    class Config:
        populate_by_name = True

# Made with Bob
