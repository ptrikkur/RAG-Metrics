# Implementation Plan: RAG Metrics Calculator Website

**Branch**: `001-rag-metrics-website` | **Date**: 2026-01-27 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-rag-metrics-website/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Build a web application that enables developers to calculate RAG (Retrieval-Augmented Generation) metrics by uploading CSV files containing query-response pairs and ground truth data. The application uses React.js for the frontend (static site) with Carbon Design System components, and Python backend for metric calculations. The system validates CSV files, computes standard RAG metrics (precision, recall, F1 score, semantic similarity), and presents results through visualizations and detailed breakdowns.

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**:
- Frontend: JavaScript/TypeScript with React 18+
- Backend: Python 3.11+

**Primary Dependencies**:
- Frontend: React 18+, Carbon Design System, Chart.js/D3.js for visualizations, Papa Parse for CSV parsing
- Backend: FastAPI, pandas, numpy, scikit-learn, sentence-transformers (for semantic similarity)

**Storage**: Browser local storage for saved analyses (client-side), no persistent backend database required

**Testing**:
- Frontend: Jest, React Testing Library
- Backend: pytest, pytest-asyncio

**Target Platform**:
- Frontend: Modern web browsers (Chrome, Firefox, Safari, Edge - latest 2 versions), desktop viewport (minimum 1024px)
- Backend: Linux/macOS server for API endpoints

**Project Type**: Web application (frontend + backend)

**Performance Goals**:
- Process and calculate metrics for datasets up to 1,000 queries within 30 seconds
- Support datasets up to 5,000 queries with calculation completing within 2 minutes
- Initial bundle size under 500KB (gzipped)
- First Contentful Paint under 2 seconds

**Constraints**:
- Maximum CSV file size: 50MB
- Client-side processing for file validation and preview
- Backend processing for metric calculations
- No user authentication required (stateless API)

**Scale/Scope**:
- Single-page application with 4-6 main views
- Support for 3 export formats (CSV, JSON, PDF)
- ~10-15 React components
- 5-8 API endpoints

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Static Build Output ✅
- **Status**: PASS
- **Rationale**: Frontend will be built as a static React application that compiles to HTML, CSS, and JavaScript. Can be deployed to any static host (Netlify, Vercel, S3, GitHub Pages). Backend API is separate and stateless.

### Component-Based Architecture ✅
- **Status**: PASS
- **Rationale**: Using React with Carbon Design System ensures component-based architecture. Components will be organized by feature (FileUpload, MetricsDisplay, ResultsTable, etc.) with clear interfaces.

### Performance Standards ✅
- **Status**: PASS
- **Rationale**:
  - Bundle size target: <500KB (gzipped) - achievable with code splitting
  - FCP target: <2s - static site with optimized assets
  - TTI target: <5s on 3G - lazy loading for heavy components (charts, PDF generation)
  - Code splitting: Implement route-based splitting and lazy load visualization libraries

### Build Requirements ✅
- **Status**: PASS
- **Rationale**: Using Vite as bundler (fast, modern, excellent React support). ES6+ with TypeScript for type safety. Production builds will be minified and optimized with source maps.

### Browser Support ✅
- **Status**: PASS
- **Rationale**: Target last 2 versions of major browsers as specified in constitution. Carbon Design System supports this range. Mobile-first responsive design (though desktop-focused per spec).

### Testing Requirements ✅
- **Status**: PASS
- **Rationale**:
  - Unit tests: Jest for business logic (metric calculations, CSV parsing)
  - Component tests: React Testing Library for UI components
  - E2E tests: Playwright for critical flows (upload → calculate → export)
  - Target: 70% code coverage minimum

### Deployment Process ✅
- **Status**: PASS
- **Rationale**: CI/CD pipeline with GitHub Actions. Preview deployments for PRs. Static frontend deployed to CDN. Backend API containerized for easy deployment and rollback.

**GATE RESULT**: ✅ ALL CHECKS PASSED - Proceed to Phase 0

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths (e.g., apps/admin, packages/something). The delivered plan must
  not include Option labels.
-->

```text
backend/
├── src/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── metrics.py
│   │   │   └── health.py
│   │   └── main.py
│   ├── services/
│   │   ├── csv_validator.py
│   │   ├── metrics_calculator.py
│   │   └── semantic_similarity.py
│   ├── models/
│   │   ├── dataset.py
│   │   └── metric_result.py
│   └── utils/
│       └── error_handlers.py
├── tests/
│   ├── unit/
│   ├── integration/
│   └── conftest.py
├── requirements.txt
└── pyproject.toml

frontend/
├── public/
│   ├── index.html
│   └── assets/
│       └── ibm-bob-logo.svg
├── src/
│   ├── components/
│   │   ├── FileUpload/
│   │   ├── MetricsDisplay/
│   │   ├── ResultsTable/
│   │   ├── DataPreview/
│   │   ├── ExportButton/
│   │   └── Header/
│   ├── pages/
│   │   ├── Home.tsx
│   │   ├── Results.tsx
│   │   └── SavedAnalyses.tsx
│   ├── services/
│   │   ├── api.ts
│   │   ├── csvParser.ts
│   │   └── storage.ts
│   ├── types/
│   │   ├── dataset.ts
│   │   └── metrics.ts
│   ├── utils/
│   │   └── formatters.ts
│   ├── App.tsx
│   └── main.tsx
├── tests/
│   ├── unit/
│   ├── component/
│   └── e2e/
├── package.json
├── vite.config.ts
└── tsconfig.json
```

**Structure Decision**: Web application structure (Option 2) selected. Frontend is a static React SPA built with Vite, using TypeScript for type safety. Backend is a Python FastAPI service providing RESTful endpoints for metric calculations. The frontend can be deployed independently to any static host, while the backend API runs as a separate service. This separation allows for independent scaling and deployment of each layer.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No violations detected. All constitution requirements are met.

## Post-Design Constitution Re-evaluation

**Date**: 2026-01-27
**Status**: ✅ ALL CHECKS PASSED

### Static Build Output ✅
- **Status**: CONFIRMED PASS
- **Implementation**: Frontend builds to static HTML/CSS/JS via Vite. Backend is stateless API with no runtime dependencies for frontend deployment.

### Component-Based Architecture ✅
- **Status**: CONFIRMED PASS
- **Implementation**: React components organized by feature (FileUpload, MetricsDisplay, ResultsTable, DataPreview, ExportButton, Header). Each component has single responsibility and clear interfaces defined in TypeScript.

### Performance Standards ✅
- **Status**: CONFIRMED PASS
- **Implementation**:
  - Bundle optimization via Vite code splitting
  - Lazy loading for charts and heavy components
  - Target bundle size: <500KB gzipped (achievable with current dependencies)
  - Route-based code splitting implemented
  - Carbon Design System components are tree-shakeable

### Build Requirements ✅
- **Status**: CONFIRMED PASS
- **Implementation**: Vite bundler with ES6+ support, TypeScript transpilation, minification, and source maps for production builds.

### Browser Support ✅
- **Status**: CONFIRMED PASS
- **Implementation**: Target last 2 versions of major browsers. Carbon Design System supports this range. Responsive design with desktop focus (min 1024px viewport).

### Testing Requirements ✅
- **Status**: CONFIRMED PASS
- **Implementation**:
  - Frontend: Jest + React Testing Library for unit/component tests
  - Backend: pytest for unit/integration tests
  - E2E: Playwright for critical user flows
  - Target: 70% code coverage minimum

### Deployment Process ✅
- **Status**: CONFIRMED PASS
- **Implementation**: CI/CD with GitHub Actions, preview deployments for PRs, static frontend to CDN, containerized backend API with rollback capability.

**FINAL GATE RESULT**: ✅ ALL CHECKS PASSED - Ready for Phase 2 (Task Breakdown)

**Design Artifacts Completed**:
- ✅ research.md - Technology decisions documented
- ✅ data-model.md - Entity definitions and relationships
- ✅ contracts/openapi.yaml - API specification
- ✅ quickstart.md - Development setup guide
- ✅ AGENTS.md - Agent context updated

**Next Phase**: Use `/speckit.tasks` to break down implementation into actionable tasks
