# Research & Technology Decisions: RAG Metrics Calculator Website

**Feature**: RAG Metrics Calculator Website  
**Branch**: `001-rag-metrics-website`  
**Date**: 2026-01-27

## Overview

This document captures research findings and technology decisions for building a web application that enables developers to calculate RAG (Retrieval-Augmented Generation) metrics from CSV data uploads.

## Technology Stack Decisions

### Frontend Framework: React 18+ with TypeScript

**Decision**: Use React 18+ with TypeScript and Vite as the build tool

**Rationale**:
- React provides excellent component reusability and ecosystem support
- TypeScript adds type safety, reducing runtime errors and improving developer experience
- Vite offers fast development server with HMR and optimized production builds
- Strong integration with Carbon Design System (IBM's design system)
- Large community and extensive documentation
- Meets constitution requirements for static build output

**Alternatives Considered**:
- Vue.js: Good framework but less mature Carbon Design System integration
- Svelte: Excellent performance but smaller ecosystem and limited Carbon support
- Angular: Too heavy for this use case, steeper learning curve

### UI Framework: Carbon Design System

**Decision**: Use Carbon Design System (@carbon/react) for all UI components

**Rationale**:
- Explicitly required in feature specification
- Provides comprehensive component library (buttons, tables, file uploaders, modals)
- Built-in accessibility features (WCAG 2.1 AA compliant)
- Consistent IBM design language
- Well-documented with React bindings
- Includes data visualization components (charts, graphs)

**Implementation Notes**:
- Use Carbon's FileUploader for CSV uploads
- Use DataTable for displaying results
- Use Carbon Charts for metric visualizations
- Use Modal for error messages and confirmations

### Backend Framework: FastAPI (Python)

**Decision**: Use FastAPI with Python 3.11+ for backend API

**Rationale**:
- FastAPI provides high performance (comparable to Node.js)
- Automatic OpenAPI documentation generation
- Built-in data validation with Pydantic
- Async support for handling concurrent requests
- Excellent for data processing tasks (pandas, numpy integration)
- Type hints improve code quality
- Easy deployment with Docker/containers

**Alternatives Considered**:
- Flask: Simpler but lacks async support and automatic documentation
- Django: Too heavy for stateless API, includes unnecessary features (ORM, admin)
- Node.js/Express: Would require different language, Python better for data science tasks

### CSV Processing

**Decision**: 
- Frontend: Papa Parse for client-side CSV parsing and preview
- Backend: pandas for server-side CSV processing and validation

**Rationale**:
- Papa Parse: Fast, reliable, handles large files, streaming support, error handling
- pandas: Industry standard for data manipulation, excellent CSV handling, integrates with numpy/scikit-learn
- Split responsibility: Client validates format/preview, server processes data

**Implementation Strategy**:
- Client-side: Parse first 10 rows for preview, validate column headers
- Server-side: Full CSV processing, data cleaning, metric calculations

### Metric Calculation Libraries

**Decision**: 
- scikit-learn for precision, recall, F1 score
- sentence-transformers for semantic similarity
- ROUGE/BLEU scores via nltk or rouge-score library

**Rationale**:
- scikit-learn: Standard library for ML metrics, well-tested, efficient
- sentence-transformers: State-of-the-art semantic similarity using transformer models
- ROUGE/BLEU: Standard metrics for text generation evaluation
- All libraries have Python bindings and good documentation

**Model Selection for Semantic Similarity**:
- Use `all-MiniLM-L6-v2` model (lightweight, fast, good quality)
- 384-dimensional embeddings
- Suitable for sentence-level similarity
- Can process 1000 queries in ~30 seconds on CPU

### Data Visualization

**Decision**: Use Carbon Charts (@carbon/charts-react)

**Rationale**:
- Native integration with Carbon Design System
- Supports bar charts, line charts, pie charts
- Accessible and responsive
- Consistent styling with rest of application
- Built on D3.js (powerful, flexible)

**Chart Types**:
- Bar charts for metric comparisons
- Line charts for per-query performance trends
- Pie charts for metric distribution
- Scatter plots for correlation analysis

### State Management

**Decision**: React Context API + hooks (useState, useReducer)

**Rationale**:
- Application state is relatively simple (uploaded data, calculated metrics, UI state)
- Context API sufficient for sharing state between components
- Avoids complexity of Redux/MobX
- Built into React, no additional dependencies
- Easy to test and maintain

**State Structure**:
- DatasetContext: Uploaded CSV data, column mappings
- MetricsContext: Calculated metrics, analysis results
- UIContext: Loading states, error messages, modal visibility

### Local Storage Strategy

**Decision**: Browser localStorage for saved analyses

**Rationale**:
- No backend database required (stateless API)
- Simple implementation with Web Storage API
- Sufficient for user's personal analysis history
- 5-10MB storage typically available (adequate for metadata)
- Store analysis metadata + download links, not full datasets

**Storage Schema**:
```json
{
  "analyses": [
    {
      "id": "uuid",
      "name": "Analysis Name",
      "timestamp": "ISO-8601",
      "datasetInfo": {
        "rowCount": 1000,
        "fileName": "data.csv"
      },
      "metrics": { "summary": "..." }
    }
  ]
}
```

### Export Functionality

**Decision**: 
- CSV: Client-side generation with Papa Parse
- JSON: Client-side generation with JSON.stringify
- PDF: Server-side generation with ReportLab (Python)

**Rationale**:
- CSV/JSON: Simple formats, client-side generation reduces server load
- PDF: Complex formatting, charts, tables - better handled server-side
- ReportLab: Mature Python library, supports charts, tables, custom layouts

### Testing Strategy

**Decision**:
- Frontend: Jest + React Testing Library + Playwright
- Backend: pytest + pytest-asyncio + httpx

**Rationale**:
- Jest: Standard React testing framework, fast, good mocking
- React Testing Library: Tests components from user perspective
- Playwright: Modern E2E testing, cross-browser support
- pytest: Python standard, excellent fixtures, async support
- httpx: Test FastAPI endpoints with async support

**Test Coverage Goals**:
- Unit tests: 80% coverage for business logic
- Component tests: All user-facing components
- Integration tests: API endpoints with mock data
- E2E tests: Critical user flows (upload → calculate → export)

### Development Tools

**Decision**:
- Frontend: ESLint + Prettier + TypeScript
- Backend: Black + isort + mypy + pylint
- Version Control: Git with conventional commits

**Rationale**:
- Consistent code formatting across team
- Type checking catches errors early
- Linting enforces best practices
- Conventional commits enable automated changelog generation

## Performance Optimization Strategies

### Bundle Size Optimization

**Strategies**:
1. Code splitting by route (React.lazy + Suspense)
2. Lazy load heavy libraries (charts, PDF generation)
3. Tree shaking with Vite
4. Compress assets with gzip/brotli
5. Use Carbon's modular imports (import specific components)

**Target**: <500KB gzipped initial bundle

### Calculation Performance

**Strategies**:
1. Process CSV in chunks for large files
2. Use Web Workers for client-side processing
3. Implement progress indicators for long calculations
4. Cache semantic similarity embeddings
5. Batch API requests for multiple queries

**Target**: 1000 queries in <30 seconds, 5000 queries in <2 minutes

### Network Optimization

**Strategies**:
1. Compress API responses (gzip)
2. Implement request debouncing
3. Use HTTP/2 for multiplexing
4. CDN for static assets
5. Implement retry logic with exponential backoff

## Security Considerations

### Data Privacy

**Approach**:
- No data persistence on server (stateless API)
- CSV files processed in memory, not stored
- Client-side storage only (user's browser)
- No user authentication required
- HTTPS required for production

### Input Validation

**Approach**:
- Client-side: File size limits, format validation
- Server-side: Pydantic models for request validation
- Sanitize CSV data to prevent injection attacks
- Rate limiting on API endpoints
- CORS configuration for allowed origins

## Deployment Strategy

### Frontend Deployment

**Approach**: Static site hosting (Netlify/Vercel/S3+CloudFront)

**Benefits**:
- Automatic SSL certificates
- Global CDN distribution
- Preview deployments for PRs
- Easy rollback
- Cost-effective

### Backend Deployment

**Approach**: Containerized deployment (Docker + Cloud Run/ECS/Kubernetes)

**Benefits**:
- Consistent environment
- Easy scaling
- Health checks and auto-restart
- Version control for deployments
- Resource limits

### CI/CD Pipeline

**Approach**: GitHub Actions

**Workflow**:
1. Run tests on PR
2. Build and deploy preview (frontend + backend)
3. Manual approval for production
4. Deploy to production
5. Run smoke tests
6. Notify team

## Open Questions & Future Considerations

### Potential Enhancements (Out of Scope for MVP)

1. **Real-time Collaboration**: Multiple users analyzing same dataset
2. **Advanced Metrics**: Custom metric definitions, A/B testing
3. **Dataset Management**: Cloud storage integration, version control
4. **API Integration**: Direct integration with RAG frameworks
5. **Mobile Support**: Responsive design for tablets/phones
6. **Batch Processing**: Process multiple CSV files simultaneously
7. **Scheduled Analysis**: Automated periodic metric calculations

### Scalability Considerations

- Current design supports up to 5000 queries per analysis
- For larger datasets, consider:
  - Streaming processing
  - Background job queue (Celery)
  - Database for intermediate results
  - Distributed computing (Dask/Ray)

## References

- [React Documentation](https://react.dev/)
- [Carbon Design System](https://carbondesignsystem.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [sentence-transformers](https://www.sbert.net/)
- [Papa Parse](https://www.papaparse.com/)
- [Vite Documentation](https://vitejs.dev/)

## Conclusion

The selected technology stack provides a solid foundation for building a performant, maintainable RAG metrics calculator. React + TypeScript + Carbon Design System ensures a consistent, accessible UI. FastAPI + Python provides robust backend processing with excellent data science library support. The architecture supports the constitution's requirements for static build output, component-based design, and performance standards.

All technical decisions are documented with clear rationale and alternatives considered. The implementation can proceed to Phase 1 (data modeling and API contracts) with confidence.