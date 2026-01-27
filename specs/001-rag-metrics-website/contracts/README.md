# API Contracts

This directory contains the API contract specifications for the RAG Metrics Calculator backend.

## Files

- **openapi.yaml**: OpenAPI 3.0.3 specification for the REST API

## API Overview

The backend API provides three main categories of endpoints:

1. **Validation** (`/api/v1/validate`): Validate CSV file structure and format
2. **Metrics** (`/api/v1/metrics/calculate`): Calculate RAG performance metrics
3. **Export** (`/api/v1/export/pdf`): Generate PDF reports

## Using the OpenAPI Specification

### View Documentation

You can view the API documentation using:

- **Swagger UI**: Import `openapi.yaml` into [Swagger Editor](https://editor.swagger.io/)
- **Redoc**: Use [Redoc](https://redocly.github.io/redoc/) for a clean documentation view
- **Postman**: Import the OpenAPI spec into Postman for testing

### Generate Client Code

Use OpenAPI Generator to create client libraries:

```bash
# TypeScript/JavaScript client
openapi-generator-cli generate -i openapi.yaml -g typescript-axios -o ../frontend/src/api/generated

# Python client (for testing)
openapi-generator-cli generate -i openapi.yaml -g python -o ../backend/tests/client
```

### Validate the Spec

```bash
# Using openapi-spec-validator
openapi-spec-validator openapi.yaml

# Using Swagger CLI
swagger-cli validate openapi.yaml
```

## API Endpoints

### Health Check
- `GET /health` - Check API service health

### Validation
- `POST /api/v1/validate` - Validate CSV file structure

### Metrics Calculation
- `POST /api/v1/metrics/calculate` - Calculate RAG metrics from data

### Export
- `POST /api/v1/export/pdf` - Generate PDF report

## Request/Response Examples

See the OpenAPI specification for detailed request/response schemas and examples.

## Authentication

The MVP does not require authentication. Future versions may implement API key authentication using the `X-API-Key` header.

## Error Handling

All endpoints return standard error responses with:
- `error`: Error code (e.g., "VALIDATION_ERROR")
- `message`: Human-readable error message
- `details`: Additional error context (optional)
- `timestamp`: ISO-8601 timestamp

## Rate Limiting

Not implemented in MVP. Future versions may implement rate limiting to prevent abuse.

## CORS

The API will be configured to accept requests from the frontend origin. In development, CORS will allow `http://localhost:3000` and `http://localhost:5173` (Vite default).

## Versioning

The API uses URL versioning (`/api/v1/`). Breaking changes will increment the version number.