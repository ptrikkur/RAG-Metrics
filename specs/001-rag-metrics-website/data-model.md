# Data Model: RAG Metrics Calculator Website

**Feature**: RAG Metrics Calculator Website  
**Branch**: `001-rag-metrics-website`  
**Date**: 2026-01-27

## Overview

This document defines the data structures and entities used throughout the RAG Metrics Calculator application. These models represent the core domain concepts and their relationships.

## Core Entities

### 1. RAGDataset

Represents uploaded CSV data containing queries, generated responses, and ground truth answers.

**Attributes**:
- `id`: string (UUID) - Unique identifier for the dataset
- `fileName`: string - Original CSV filename
- `uploadTimestamp`: datetime (ISO-8601) - When the file was uploaded
- `rowCount`: integer - Number of data rows (excluding header)
- `columnMappings`: ColumnMapping - Maps CSV columns to required fields
- `data`: DataRow[] - Array of parsed data rows
- `validationStatus`: ValidationStatus - Result of CSV validation
- `metadata`: DatasetMetadata - Additional dataset information

**Validation Rules**:
- `fileName` must not be empty
- `rowCount` must be > 0 and <= 10,000
- `data` array length must equal `rowCount`
- `columnMappings` must map all required fields (query, response, groundTruth)

**State Transitions**:
```
UPLOADING → VALIDATING → VALID | INVALID
VALID → PROCESSING → PROCESSED
```

**Example**:
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "fileName": "rag_evaluation_data.csv",
  "uploadTimestamp": "2026-01-27T12:00:00Z",
  "rowCount": 1000,
  "columnMappings": {
    "query": "question",
    "response": "generated_answer",
    "groundTruth": "correct_answer"
  },
  "validationStatus": "VALID",
  "metadata": {
    "fileSize": 2048576,
    "encoding": "UTF-8",
    "delimiter": ","
  }
}
```

### 2. ColumnMapping

Maps CSV column names to required field names.

**Attributes**:
- `query`: string - Column name containing query text
- `response`: string - Column name containing generated responses
- `groundTruth`: string - Column name containing ground truth answers
- `metadata`: object (optional) - Additional column mappings for custom fields

**Validation Rules**:
- All three required fields must be non-empty strings
- Column names must exist in the CSV header
- Column names must be unique (no duplicate mappings)

**Example**:
```json
{
  "query": "user_question",
  "response": "ai_response",
  "groundTruth": "expected_answer",
  "metadata": {
    "queryId": "id",
    "timestamp": "created_at"
  }
}
```

### 3. DataRow

Represents a single row of RAG evaluation data.

**Attributes**:
- `rowIndex`: integer - Original row number in CSV (1-based)
- `query`: string - The input query/question
- `response`: string - The generated response from RAG system
- `groundTruth`: string - The correct/expected answer
- `metadata`: object (optional) - Additional fields from CSV

**Validation Rules**:
- `query`, `response`, and `groundTruth` must not be empty strings
- `rowIndex` must be > 0
- Text fields should be trimmed of leading/trailing whitespace

**Example**:
```json
{
  "rowIndex": 1,
  "query": "What is the capital of France?",
  "response": "The capital of France is Paris.",
  "groundTruth": "Paris",
  "metadata": {
    "queryId": "Q001",
    "timestamp": "2026-01-20T10:30:00Z"
  }
}
```

### 4. MetricResult

Represents calculated performance metrics for a dataset.

**Attributes**:
- `id`: string (UUID) - Unique identifier for this metric calculation
- `datasetId`: string (UUID) - Reference to the RAGDataset
- `calculationTimestamp`: datetime (ISO-8601) - When metrics were calculated
- `aggregateMetrics`: AggregateMetrics - Overall performance metrics
- `perQueryMetrics`: QueryMetrics[] - Individual query-level metrics
- `calculationTime`: number - Time taken to calculate (seconds)
- `metricTypes`: string[] - List of calculated metric types

**Validation Rules**:
- `datasetId` must reference a valid RAGDataset
- `aggregateMetrics` must contain at least one metric
- `perQueryMetrics` length must equal dataset rowCount
- `calculationTime` must be > 0

**Example**:
```json
{
  "id": "660e8400-e29b-41d4-a716-446655440001",
  "datasetId": "550e8400-e29b-41d4-a716-446655440000",
  "calculationTimestamp": "2026-01-27T12:05:00Z",
  "aggregateMetrics": {
    "precision": 0.85,
    "recall": 0.82,
    "f1Score": 0.835,
    "semanticSimilarity": 0.78
  },
  "calculationTime": 28.5,
  "metricTypes": ["precision", "recall", "f1Score", "semanticSimilarity"]
}
```

### 5. AggregateMetrics

Overall performance metrics across all queries.

**Attributes**:
- `precision`: number (0-1) - Precision score
- `recall`: number (0-1) - Recall score
- `f1Score`: number (0-1) - F1 score (harmonic mean of precision and recall)
- `semanticSimilarity`: number (0-1) - Average semantic similarity score
- `bleuScore`: number (0-1, optional) - BLEU score for text generation
- `rougeScore`: object (optional) - ROUGE scores (ROUGE-1, ROUGE-2, ROUGE-L)
- `exactMatchRate`: number (0-1) - Percentage of exact matches

**Validation Rules**:
- All metric values must be between 0 and 1 (inclusive)
- `f1Score` should equal 2 * (precision * recall) / (precision + recall)
- At least one metric must be present

**Example**:
```json
{
  "precision": 0.85,
  "recall": 0.82,
  "f1Score": 0.835,
  "semanticSimilarity": 0.78,
  "bleuScore": 0.72,
  "rougeScore": {
    "rouge1": 0.75,
    "rouge2": 0.68,
    "rougeL": 0.73
  },
  "exactMatchRate": 0.15
}
```

### 6. QueryMetrics

Performance metrics for a single query.

**Attributes**:
- `rowIndex`: integer - Reference to DataRow
- `query`: string - The query text (for reference)
- `precision`: number (0-1) - Query-level precision
- `recall`: number (0-1) - Query-level recall
- `f1Score`: number (0-1) - Query-level F1 score
- `semanticSimilarity`: number (0-1) - Semantic similarity score
- `responseLength`: integer - Length of generated response (characters)
- `groundTruthLength`: integer - Length of ground truth (characters)
- `issues`: string[] (optional) - Identified issues with this query

**Validation Rules**:
- `rowIndex` must match a valid DataRow
- All metric values must be between 0 and 1
- `responseLength` and `groundTruthLength` must be >= 0

**Example**:
```json
{
  "rowIndex": 1,
  "query": "What is the capital of France?",
  "precision": 1.0,
  "recall": 1.0,
  "f1Score": 1.0,
  "semanticSimilarity": 0.95,
  "responseLength": 32,
  "groundTruthLength": 5,
  "issues": []
}
```

### 7. SavedAnalysis

Represents a stored analysis session for later retrieval.

**Attributes**:
- `id`: string (UUID) - Unique identifier
- `name`: string - User-provided name for the analysis
- `description`: string (optional) - User-provided description
- `createdTimestamp`: datetime (ISO-8601) - When analysis was saved
- `datasetInfo`: DatasetInfo - Summary of the dataset
- `metricsSummary`: AggregateMetrics - Summary of calculated metrics
- `exportUrls`: ExportUrls (optional) - Links to exported files

**Validation Rules**:
- `name` must not be empty and <= 100 characters
- `description` must be <= 500 characters if provided
- `datasetInfo` and `metricsSummary` must be present

**Storage**: Browser localStorage (JSON serialized)

**Example**:
```json
{
  "id": "770e8400-e29b-41d4-a716-446655440002",
  "name": "Production RAG v2.1 Evaluation",
  "description": "Evaluation of RAG system after implementing semantic caching",
  "createdTimestamp": "2026-01-27T12:10:00Z",
  "datasetInfo": {
    "fileName": "prod_eval_jan2026.csv",
    "rowCount": 1000,
    "uploadTimestamp": "2026-01-27T12:00:00Z"
  },
  "metricsSummary": {
    "precision": 0.85,
    "recall": 0.82,
    "f1Score": 0.835,
    "semanticSimilarity": 0.78
  }
}
```

### 8. DatasetInfo

Summary information about a dataset (used in SavedAnalysis).

**Attributes**:
- `fileName`: string - Original CSV filename
- `rowCount`: integer - Number of data rows
- `uploadTimestamp`: datetime (ISO-8601) - When uploaded
- `fileSize`: integer (optional) - File size in bytes

**Example**:
```json
{
  "fileName": "evaluation_data.csv",
  "rowCount": 1000,
  "uploadTimestamp": "2026-01-27T12:00:00Z",
  "fileSize": 2048576
}
```

### 9. ValidationStatus

Represents the validation state of a dataset.

**Type**: Enum

**Values**:
- `PENDING`: Validation not yet started
- `VALIDATING`: Validation in progress
- `VALID`: Dataset passed all validation checks
- `INVALID`: Dataset failed validation

**Associated Data** (when INVALID):
- `errors`: ValidationError[] - List of validation errors

**Example**:
```json
{
  "status": "INVALID",
  "errors": [
    {
      "code": "MISSING_COLUMN",
      "message": "Required column 'ground_truth' not found in CSV",
      "severity": "ERROR"
    },
    {
      "code": "EMPTY_VALUES",
      "message": "Row 45 has empty value in 'response' column",
      "severity": "WARNING",
      "rowIndex": 45
    }
  ]
}
```

### 10. ValidationError

Represents a validation error or warning.

**Attributes**:
- `code`: string - Error code (e.g., "MISSING_COLUMN", "EMPTY_VALUES")
- `message`: string - Human-readable error message
- `severity`: "ERROR" | "WARNING" - Severity level
- `rowIndex`: integer (optional) - Row number where error occurred
- `columnName`: string (optional) - Column name where error occurred

**Example**:
```json
{
  "code": "INVALID_FORMAT",
  "message": "CSV file is not properly formatted",
  "severity": "ERROR"
}
```

### 11. ExportUrls

URLs or blob references for exported files.

**Attributes**:
- `csv`: string (optional) - URL/blob for CSV export
- `json`: string (optional) - URL/blob for JSON export
- `pdf`: string (optional) - URL/blob for PDF export

**Example**:
```json
{
  "csv": "blob:http://localhost:3000/abc123",
  "json": "blob:http://localhost:3000/def456",
  "pdf": "https://api.example.com/exports/ghi789.pdf"
}
```

### 12. DatasetMetadata

Additional metadata about the dataset.

**Attributes**:
- `fileSize`: integer - File size in bytes
- `encoding`: string - Character encoding (e.g., "UTF-8")
- `delimiter`: string - CSV delimiter character
- `hasHeader`: boolean - Whether CSV has header row
- `columnCount`: integer - Number of columns in CSV

**Example**:
```json
{
  "fileSize": 2048576,
  "encoding": "UTF-8",
  "delimiter": ",",
  "hasHeader": true,
  "columnCount": 5
}
```

## Entity Relationships

```
RAGDataset (1) ──< (1) MetricResult
    │
    └──< (many) DataRow

MetricResult (1) ──< (many) QueryMetrics

SavedAnalysis (1) ──> (1) DatasetInfo
                 └──> (1) AggregateMetrics

RAGDataset (1) ──> (1) ColumnMapping
              └──> (1) ValidationStatus
              └──> (1) DatasetMetadata
```

## Data Flow

1. **Upload Phase**:
   - User uploads CSV → RAGDataset created (UPLOADING state)
   - CSV parsed → DataRow[] populated
   - Validation runs → ValidationStatus updated (VALID/INVALID)

2. **Calculation Phase**:
   - User triggers calculation → RAGDataset state: PROCESSING
   - Backend processes DataRow[] → QueryMetrics[] calculated
   - Aggregate metrics computed → MetricResult created
   - RAGDataset state: PROCESSED

3. **Storage Phase**:
   - User saves analysis → SavedAnalysis created
   - DatasetInfo and AggregateMetrics extracted
   - Stored in browser localStorage

4. **Export Phase**:
   - User requests export → ExportUrls generated
   - Files created (CSV/JSON client-side, PDF server-side)
   - URLs stored in SavedAnalysis

## Validation Summary

### Required Fields
- RAGDataset: id, fileName, uploadTimestamp, rowCount, columnMappings, data
- DataRow: rowIndex, query, response, groundTruth
- MetricResult: id, datasetId, calculationTimestamp, aggregateMetrics
- SavedAnalysis: id, name, createdTimestamp, datasetInfo, metricsSummary

### Constraints
- All metric values: 0 <= value <= 1
- Row counts: 1 <= count <= 10,000
- File size: <= 50MB
- Text lengths: query/response/groundTruth <= 10,000 characters each

### Referential Integrity
- MetricResult.datasetId → RAGDataset.id
- QueryMetrics.rowIndex → DataRow.rowIndex
- SavedAnalysis references immutable snapshots (no foreign keys)

## Storage Considerations

### Client-Side (Browser)
- **localStorage**: SavedAnalysis[] (metadata only, ~5-10MB limit)
- **sessionStorage**: Current RAGDataset and MetricResult (cleared on tab close)
- **IndexedDB**: Not used in MVP (future consideration for large datasets)

### Server-Side
- **No persistent storage**: Stateless API
- **In-memory**: Temporary storage during calculation
- **File system**: Temporary PDF generation (cleaned up after download)

## Future Enhancements

1. **Versioning**: Track dataset and metric versions
2. **Comparison**: Compare metrics across multiple analyses
3. **Custom Metrics**: User-defined metric calculations
4. **Annotations**: User comments on specific queries
5. **Sharing**: Export analysis links for team collaboration
6. **History**: Track changes to datasets over time

## Conclusion

This data model provides a solid foundation for the RAG Metrics Calculator application. All entities are well-defined with clear validation rules and relationships. The model supports the core workflows (upload, validate, calculate, save, export) while maintaining simplicity and avoiding unnecessary complexity.