"""
Pydantic models for metric calculation results.
"""
from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any


class AggregateMetrics(BaseModel):
    """Overall performance metrics across all queries."""
    precision: float = Field(..., ge=0.0, le=1.0, description="Precision score")
    recall: float = Field(..., ge=0.0, le=1.0, description="Recall score")
    f1Score: float = Field(..., alias="f1Score", ge=0.0, le=1.0, description="F1 score")
    semanticSimilarity: float = Field(..., alias="semanticSimilarity", ge=0.0, le=1.0, description="Semantic similarity score")
    bleuScore: Optional[float] = Field(default=None, alias="bleuScore", ge=0.0, le=1.0, description="BLEU score")
    rougeScore: Optional[Dict[str, float]] = Field(default=None, alias="rougeScore", description="ROUGE scores")
    exactMatchRate: Optional[float] = Field(default=None, alias="exactMatchRate", ge=0.0, le=1.0, description="Exact match rate")
    
    class Config:
        populate_by_name = True


class QueryMetrics(BaseModel):
    """Performance metrics for a single query."""
    rowIndex: int = Field(..., alias="rowIndex", ge=1, description="Row number reference")
    query: str = Field(..., description="Query text for reference")
    precision: float = Field(..., ge=0.0, le=1.0, description="Query-level precision")
    recall: float = Field(..., ge=0.0, le=1.0, description="Query-level recall")
    f1Score: float = Field(..., alias="f1Score", ge=0.0, le=1.0, description="Query-level F1 score")
    semanticSimilarity: float = Field(..., alias="semanticSimilarity", ge=0.0, le=1.0, description="Semantic similarity")
    responseLength: int = Field(..., alias="responseLength", ge=0, description="Response length in characters")
    groundTruthLength: int = Field(..., alias="groundTruthLength", ge=0, description="Ground truth length in characters")
    issues: Optional[List[str]] = Field(default=None, description="Identified issues")
    
    class Config:
        populate_by_name = True


class MetricResult(BaseModel):
    """Complete metric calculation result."""
    id: str = Field(..., description="Unique identifier (UUID)")
    datasetId: str = Field(..., alias="datasetId", description="Reference to RAGDataset")
    calculationTimestamp: str = Field(..., alias="calculationTimestamp", description="Calculation timestamp (ISO-8601)")
    aggregateMetrics: AggregateMetrics = Field(..., alias="aggregateMetrics", description="Overall metrics")
    perQueryMetrics: List[QueryMetrics] = Field(..., alias="perQueryMetrics", description="Per-query metrics")
    calculationTime: float = Field(..., alias="calculationTime", gt=0, description="Calculation time in seconds")
    metricTypes: List[str] = Field(..., alias="metricTypes", description="List of calculated metric types")
    
    class Config:
        populate_by_name = True


class MetricsCalculationRequest(BaseModel):
    """Request to calculate metrics."""
    data: List[Dict[str, Any]] = Field(..., description="Array of data rows")
    columnMappings: Dict[str, str] = Field(..., alias="columnMappings", description="Column mappings")
    metricTypes: Optional[List[str]] = Field(default=None, alias="metricTypes", description="Specific metrics to calculate")
    
    class Config:
        populate_by_name = True


class MetricsCalculationResponse(BaseModel):
    """Response from metrics calculation."""
    id: str = Field(..., description="Unique identifier")
    calculationTimestamp: str = Field(..., alias="calculationTimestamp", description="Timestamp")
    aggregateMetrics: AggregateMetrics = Field(..., alias="aggregateMetrics", description="Aggregate metrics")
    perQueryMetrics: List[QueryMetrics] = Field(..., alias="perQueryMetrics", description="Per-query metrics")
    calculationTime: float = Field(..., alias="calculationTime", description="Calculation time in seconds")
    metricTypes: List[str] = Field(..., alias="metricTypes", description="Calculated metric types")
    
    class Config:
        populate_by_name = True


class DatasetInfo(BaseModel):
    """Summary information about a dataset."""
    fileName: str = Field(..., alias="fileName", description="Original filename")
    rowCount: int = Field(..., alias="rowCount", ge=1, description="Number of rows")
    uploadTimestamp: str = Field(..., alias="uploadTimestamp", description="Upload timestamp")
    fileSize: Optional[int] = Field(default=None, alias="fileSize", description="File size in bytes")
    
    class Config:
        populate_by_name = True


class PDFExportRequest(BaseModel):
    """Request to generate PDF report."""
    datasetInfo: DatasetInfo = Field(..., alias="datasetInfo", description="Dataset information")
    aggregateMetrics: AggregateMetrics = Field(..., alias="aggregateMetrics", description="Aggregate metrics")
    perQueryMetrics: List[QueryMetrics] = Field(..., alias="perQueryMetrics", description="Per-query metrics")
    includeCharts: bool = Field(default=True, alias="includeCharts", description="Include visualizations")
    includeDetailedBreakdown: bool = Field(default=True, alias="includeDetailedBreakdown", description="Include per-query details")
    
    class Config:
        populate_by_name = True

# Made with Bob
