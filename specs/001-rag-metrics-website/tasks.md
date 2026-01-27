# Tasks: RAG Metrics Calculator Website

**Input**: Design documents from `/specs/001-rag-metrics-website/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/openapi.yaml

**Tests**: Tests are NOT explicitly requested in the specification, so test tasks are excluded. Focus is on implementation.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- **Web app structure**: `backend/src/`, `frontend/src/`
- Backend: Python FastAPI
- Frontend: React + TypeScript + Vite

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create backend directory structure: backend/src/{api,services,models,utils}, backend/tests/{unit,integration}
- [x] T002 Create frontend directory structure: frontend/src/{components,pages,services,types,utils}, frontend/tests/{unit,component,e2e}
- [x] T003 Initialize Python project with requirements.txt in backend/
- [x] T004 Initialize Node.js project with package.json in frontend/
- [x] T005 [P] Configure Python linting tools (black, isort, mypy, pylint) in backend/pyproject.toml
- [x] T006 [P] Configure TypeScript and ESLint in frontend/tsconfig.json and frontend/.eslintrc.js
- [x] T007 [P] Setup Vite configuration in frontend/vite.config.ts
- [x] T008 [P] Create backend/.env.example with environment variable templates
- [x] T009 [P] Create frontend/.env.example with VITE_API_BASE_URL template
- [x] T010 [P] Add IBM Bob logo SVG to frontend/public/assets/ibm-bob-logo.svg
- [x] T011 [P] Create frontend/public/index.html with Carbon Design System setup

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

### Backend Foundation

- [ ] T012 Create FastAPI application entry point in backend/src/api/main.py with CORS configuration
- [ ] T013 [P] Implement health check endpoint in backend/src/api/routes/health.py
- [ ] T014 [P] Create error handler utilities in backend/src/utils/error_handlers.py
- [ ] T015 [P] Create base Pydantic models for requests/responses in backend/src/models/dataset.py
- [ ] T016 [P] Create base Pydantic models for metrics in backend/src/models/metric_result.py
- [ ] T017 Setup logging configuration in backend/src/utils/logger.py

### Frontend Foundation

- [ ] T018 Create React App component with routing in frontend/src/App.tsx
- [ ] T019 [P] Create main entry point in frontend/src/main.tsx
- [ ] T020 [P] Setup API client service in frontend/src/services/api.ts with axios configuration
- [ ] T021 [P] Create TypeScript types for Dataset in frontend/src/types/dataset.ts
- [ ] T022 [P] Create TypeScript types for Metrics in frontend/src/types/metrics.ts
- [ ] T023 [P] Create Header component with IBM Bob logo in frontend/src/components/Header/Header.tsx
- [ ] T024 [P] Create utility formatters in frontend/src/utils/formatters.ts

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Upload CSV and Calculate Basic RAG Metrics (Priority: P1) 🎯 MVP

**Goal**: Enable developers to upload CSV files, validate them, calculate basic RAG metrics (precision, recall, F1 score), and view results with visualizations

**Independent Test**: Upload a valid CSV file with query-response-groundtruth data, click "Calculate Metrics", and verify that precision, recall, and F1 scores are displayed with visualizations

### Backend Implementation for US1

- [ ] T025 [P] [US1] Create CSV validation service in backend/src/services/csv_validator.py
- [ ] T026 [P] [US1] Create metrics calculator service in backend/src/services/metrics_calculator.py
- [ ] T027 [US1] Implement /api/v1/validate endpoint in backend/src/api/routes/metrics.py
- [ ] T028 [US1] Implement /api/v1/metrics/calculate endpoint in backend/src/api/routes/metrics.py
- [ ] T029 [US1] Add CSV file upload handling with size validation (50MB limit) in backend/src/api/routes/metrics.py
- [ ] T030 [US1] Implement precision calculation logic in backend/src/services/metrics_calculator.py
- [ ] T031 [US1] Implement recall calculation logic in backend/src/services/metrics_calculator.py
- [ ] T032 [US1] Implement F1 score calculation logic in backend/src/services/metrics_calculator.py
- [ ] T033 [US1] Add error handling for invalid CSV formats in backend/src/services/csv_validator.py
- [ ] T034 [US1] Add error handling for missing required columns in backend/src/services/csv_validator.py

### Frontend Implementation for US1

- [ ] T035 [P] [US1] Create FileUpload component in frontend/src/components/FileUpload/FileUpload.tsx
- [ ] T036 [P] [US1] Create DataPreview component in frontend/src/components/DataPreview/DataPreview.tsx
- [ ] T037 [P] [US1] Create MetricsDisplay component in frontend/src/components/MetricsDisplay/MetricsDisplay.tsx
- [ ] T038 [US1] Create CSV parser service in frontend/src/services/csvParser.ts using Papa Parse
- [ ] T039 [US1] Create Home page component in frontend/src/pages/Home.tsx
- [ ] T040 [US1] Create Results page component in frontend/src/pages/Results.tsx
- [ ] T041 [US1] Implement file upload UI with Carbon FileUploader in frontend/src/components/FileUpload/FileUpload.tsx
- [ ] T042 [US1] Implement CSV preview table with first 10 rows in frontend/src/components/DataPreview/DataPreview.tsx
- [ ] T043 [US1] Implement column mapping UI for CSV headers in frontend/src/components/FileUpload/FileUpload.tsx
- [ ] T044 [US1] Implement "Calculate Metrics" button with loading state in frontend/src/pages/Home.tsx
- [ ] T045 [US1] Implement metrics visualization using Carbon Charts in frontend/src/components/MetricsDisplay/MetricsDisplay.tsx
- [ ] T046 [US1] Display precision, recall, F1 score with explanations in frontend/src/components/MetricsDisplay/MetricsDisplay.tsx
- [ ] T047 [US1] Add error message display for validation failures in frontend/src/pages/Home.tsx
- [ ] T048 [US1] Add progress indicator during metric calculation in frontend/src/pages/Home.tsx

**Checkpoint**: At this point, User Story 1 should be fully functional - users can upload CSV, validate, calculate basic metrics, and view results

---

## Phase 4: User Story 2 - View Detailed Metric Breakdowns (Priority: P2)

**Goal**: Enable developers to view per-query performance metrics, sort/filter results, and drill down into individual query details

**Independent Test**: After calculating metrics for a dataset, navigate to detailed view and verify that individual query metrics are displayed, sortable, and clickable for details

### Backend Implementation for US2

- [ ] T049 [US2] Add per-query metrics calculation in backend/src/services/metrics_calculator.py
- [ ] T050 [US2] Extend MetricResult model to include perQueryMetrics array in backend/src/models/metric_result.py
- [ ] T051 [US2] Update /api/v1/metrics/calculate response to include per-query data in backend/src/api/routes/metrics.py

### Frontend Implementation for US2

- [ ] T052 [P] [US2] Create ResultsTable component in frontend/src/components/ResultsTable/ResultsTable.tsx
- [ ] T053 [US2] Implement per-query metrics table with Carbon DataTable in frontend/src/components/ResultsTable/ResultsTable.tsx
- [ ] T054 [US2] Add sorting functionality for metric columns in frontend/src/components/ResultsTable/ResultsTable.tsx
- [ ] T055 [US2] Add filtering functionality for metric values in frontend/src/components/ResultsTable/ResultsTable.tsx
- [ ] T056 [US2] Implement query detail modal with Carbon Modal in frontend/src/components/ResultsTable/QueryDetailModal.tsx
- [ ] T057 [US2] Display query text, response, ground truth, and scores in detail modal in frontend/src/components/ResultsTable/QueryDetailModal.tsx
- [ ] T058 [US2] Add navigation between aggregate and detailed views in frontend/src/pages/Results.tsx
- [ ] T059 [US2] Implement pagination for large datasets in frontend/src/components/ResultsTable/ResultsTable.tsx

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently - users can view both aggregate and detailed metrics

---

## Phase 5: User Story 3 - Download Metric Reports (Priority: P3)

**Goal**: Enable developers to export calculated metrics in CSV, JSON, and PDF formats for sharing and documentation

**Independent Test**: After calculating metrics, click "Export Results", select a format (CSV/JSON/PDF), and verify the downloaded file contains all metrics and visualizations

### Backend Implementation for US3

- [ ] T060 [P] [US3] Implement PDF generation service in backend/src/services/pdf_generator.py using ReportLab
- [ ] T061 [US3] Implement /api/v1/export/pdf endpoint in backend/src/api/routes/metrics.py
- [ ] T062 [US3] Add chart generation for PDF reports in backend/src/services/pdf_generator.py
- [ ] T063 [US3] Add table formatting for per-query metrics in PDF in backend/src/services/pdf_generator.py
- [ ] T064 [US3] Add summary statistics section to PDF reports in backend/src/services/pdf_generator.py

### Frontend Implementation for US3

- [ ] T065 [P] [US3] Create ExportButton component in frontend/src/components/ExportButton/ExportButton.tsx
- [ ] T066 [US3] Implement CSV export (client-side) using Papa Parse in frontend/src/services/csvParser.ts
- [ ] T067 [US3] Implement JSON export (client-side) in frontend/src/components/ExportButton/ExportButton.tsx
- [ ] T068 [US3] Implement PDF export (server-side) API call in frontend/src/services/api.ts
- [ ] T069 [US3] Add export format selection dropdown in frontend/src/components/ExportButton/ExportButton.tsx
- [ ] T070 [US3] Add download progress indicator in frontend/src/components/ExportButton/ExportButton.tsx
- [ ] T071 [US3] Handle export errors and display user-friendly messages in frontend/src/components/ExportButton/ExportButton.tsx

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently - users can export results in multiple formats

---

## Phase 6: User Story 4 - Save and Load Previous Analyses (Priority: P3)

**Goal**: Enable developers to save analysis results to browser localStorage and load them later for comparison across RAG system versions

**Independent Test**: Calculate metrics, save the analysis with a name, close browser, reopen, and verify the saved analysis can be loaded with all data intact

### Frontend Implementation for US4

- [ ] T072 [P] [US4] Create storage service for localStorage operations in frontend/src/services/storage.ts
- [ ] T073 [P] [US4] Create SavedAnalyses page component in frontend/src/pages/SavedAnalyses.tsx
- [ ] T074 [US4] Implement save analysis functionality in frontend/src/services/storage.ts
- [ ] T075 [US4] Implement load analysis functionality in frontend/src/services/storage.ts
- [ ] T076 [US4] Implement delete analysis functionality in frontend/src/services/storage.ts
- [ ] T077 [US4] Create "Save Analysis" button with name input modal in frontend/src/pages/Results.tsx
- [ ] T078 [US4] Display list of saved analyses with dates and names in frontend/src/pages/SavedAnalyses.tsx
- [ ] T079 [US4] Implement "Load" button for each saved analysis in frontend/src/pages/SavedAnalyses.tsx
- [ ] T080 [US4] Implement "Delete" button for each saved analysis in frontend/src/pages/SavedAnalyses.tsx
- [ ] T081 [US4] Add navigation link to SavedAnalyses page in frontend/src/components/Header/Header.tsx
- [ ] T082 [US4] Restore all metrics and visualizations when loading saved analysis in frontend/src/pages/Results.tsx
- [ ] T083 [US4] Add localStorage quota check and warning in frontend/src/services/storage.ts

**Checkpoint**: All user stories should now be independently functional - complete feature set delivered

---

## Phase 7: Advanced Metrics & Polish

**Purpose**: Add semantic similarity calculations and cross-cutting improvements

### Backend Advanced Metrics

- [ ] T084 [P] Create semantic similarity service in backend/src/services/semantic_similarity.py using sentence-transformers
- [ ] T085 Integrate semantic similarity into metrics calculation in backend/src/services/metrics_calculator.py
- [ ] T086 [P] Add BLEU score calculation in backend/src/services/metrics_calculator.py
- [ ] T087 [P] Add ROUGE score calculation in backend/src/services/metrics_calculator.py
- [ ] T088 Update aggregate metrics to include semantic similarity in backend/src/models/metric_result.py
- [ ] T089 Update per-query metrics to include semantic similarity in backend/src/models/metric_result.py

### Frontend Polish

- [ ] T090 [P] Add semantic similarity visualization to MetricsDisplay in frontend/src/components/MetricsDisplay/MetricsDisplay.tsx
- [ ] T091 [P] Add BLEU/ROUGE score displays in frontend/src/components/MetricsDisplay/MetricsDisplay.tsx
- [ ] T092 [P] Implement responsive design for mobile viewports in frontend/src/App.tsx
- [ ] T093 [P] Add loading skeletons for better UX in frontend/src/components/MetricsDisplay/MetricsDisplay.tsx
- [ ] T094 [P] Add tooltips with metric explanations using Carbon Tooltip in frontend/src/components/MetricsDisplay/MetricsDisplay.tsx
- [ ] T095 [P] Implement dark mode support with Carbon themes in frontend/src/App.tsx

### Documentation & Validation

- [ ] T096 [P] Create API documentation using FastAPI auto-docs in backend/src/api/main.py
- [ ] T097 [P] Add inline code comments for complex algorithms in backend/src/services/
- [ ] T098 [P] Create README.md in backend/ with setup instructions
- [ ] T099 [P] Create README.md in frontend/ with setup instructions
- [ ] T100 Run quickstart.md validation to ensure setup instructions work
- [ ] T101 [P] Add error boundary component in frontend/src/components/ErrorBoundary.tsx
- [ ] T102 [P] Implement analytics tracking (optional) in frontend/src/utils/analytics.ts

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P3)
- **Advanced Metrics & Polish (Phase 7)**: Depends on User Story 1 (P1) being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Builds on US1 but independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Requires US1 metrics to export
- **User Story 4 (P3)**: Can start after Foundational (Phase 2) - Requires US1 metrics to save

### Within Each User Story

- Backend models before services
- Backend services before API endpoints
- Frontend types before components
- Frontend components before pages
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Components within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Backend - Launch all parallel tasks together:
Task T025: "Create CSV validation service in backend/src/services/csv_validator.py"
Task T026: "Create metrics calculator service in backend/src/services/metrics_calculator.py"

# Frontend - Launch all parallel components together:
Task T035: "Create FileUpload component in frontend/src/components/FileUpload/FileUpload.tsx"
Task T036: "Create DataPreview component in frontend/src/components/DataPreview/DataPreview.tsx"
Task T037: "Create MetricsDisplay component in frontend/src/components/MetricsDisplay/MetricsDisplay.tsx"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T011)
2. Complete Phase 2: Foundational (T012-T024) - CRITICAL - blocks all stories
3. Complete Phase 3: User Story 1 (T025-T048)
4. **STOP and VALIDATE**: Test User Story 1 independently
   - Upload CSV file
   - Validate format
   - Calculate metrics
   - View results with visualizations
5. Deploy/demo if ready

**MVP Deliverable**: Working RAG metrics calculator with CSV upload and basic metric calculation

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo (detailed breakdowns)
4. Add User Story 3 → Test independently → Deploy/Demo (export functionality)
5. Add User Story 4 → Test independently → Deploy/Demo (save/load)
6. Add Advanced Metrics → Test → Deploy/Demo (semantic similarity, BLEU, ROUGE)
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together (T001-T024)
2. Once Foundational is done:
   - Developer A: User Story 1 Backend (T025-T034)
   - Developer B: User Story 1 Frontend (T035-T048)
   - Developer C: User Story 2 (T049-T059) - can start in parallel
3. Stories complete and integrate independently

### Recommended Order for Solo Developer

1. Phase 1: Setup (1-2 hours)
2. Phase 2: Foundational (2-3 hours)
3. Phase 3: User Story 1 Backend (3-4 hours)
4. Phase 3: User Story 1 Frontend (4-5 hours)
5. **TEST MVP** - Validate User Story 1 works end-to-end
6. Phase 4: User Story 2 (3-4 hours)
7. Phase 5: User Story 3 (2-3 hours)
8. Phase 6: User Story 4 (2-3 hours)
9. Phase 7: Advanced Metrics & Polish (4-6 hours)

**Total Estimated Time**: 24-32 hours for complete implementation

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Backend uses Python 3.11+, FastAPI, pandas, scikit-learn, sentence-transformers
- Frontend uses React 18+, TypeScript, Vite, Carbon Design System
- No persistent database - stateless API with browser localStorage for saved analyses
- Maximum CSV file size: 50MB
- Target: Process 1000 queries in <30 seconds, 5000 queries in <2 minutes
- All paths are relative to repository root
- Follow code style guidelines in AGENTS.md