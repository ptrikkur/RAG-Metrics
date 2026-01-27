# Feature Specification: RAG Metrics Calculator Website

**Feature Branch**: `001-rag-metrics-website`  
**Created**: 2026-01-27  
**Status**: Draft  
**Input**: User description: "I am building a website that will make it easy for developers to calculate RAG Metrics. It should have a facility to upload data through a csv file. The UI should use Carbon Framework."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Upload CSV and Calculate Basic RAG Metrics (Priority: P1)

A developer needs to quickly evaluate their RAG system's performance by uploading a CSV file containing query-response pairs and ground truth data, then viewing calculated metrics.

**Why this priority**: This is the core value proposition - enabling developers to calculate RAG metrics without writing code. Without this, the website has no purpose.

**Independent Test**: Can be fully tested by uploading a valid CSV file with sample RAG data and verifying that basic metrics (precision, recall, F1 score) are calculated and displayed correctly.

**Acceptance Scenarios**:

1. **Given** a developer has a CSV file with columns for queries, generated responses, and ground truth answers, **When** they upload the file through the website, **Then** the system validates the file format and displays a preview of the data
2. **Given** a valid CSV file has been uploaded, **When** the developer clicks "Calculate Metrics", **Then** the system computes and displays basic RAG metrics including precision, recall, and F1 score
3. **Given** metrics have been calculated, **When** the developer views the results, **Then** they see clear visualizations and numerical values for each metric with explanations

---

### User Story 2 - View Detailed Metric Breakdowns (Priority: P2)

A developer wants to understand not just overall metrics but also per-query performance to identify specific weaknesses in their RAG system.

**Why this priority**: Provides actionable insights beyond aggregate metrics, helping developers improve their systems. Builds on P1 functionality.

**Independent Test**: Can be tested by uploading a CSV with multiple queries and verifying that the system displays individual query performance alongside aggregate metrics.

**Acceptance Scenarios**:

1. **Given** metrics have been calculated for a dataset, **When** the developer navigates to the detailed view, **Then** they see a breakdown of metrics for each individual query
2. **Given** the detailed breakdown is displayed, **When** the developer clicks on a specific query, **Then** they see the original query, generated response, ground truth, and calculated scores for that query
3. **Given** multiple queries are displayed, **When** the developer sorts or filters by metric values, **Then** the list updates to show queries ordered by the selected metric

---

### User Story 3 - Download Metric Reports (Priority: P3)

A developer wants to export calculated metrics and analysis results to share with their team or include in documentation.

**Why this priority**: Enhances usability by enabling collaboration and record-keeping. Not essential for initial value delivery.

**Independent Test**: Can be tested by calculating metrics for a dataset and verifying that the export function generates a downloadable report in common formats (CSV, PDF, or JSON).

**Acceptance Scenarios**:

1. **Given** metrics have been calculated, **When** the developer clicks "Export Results", **Then** they can choose between CSV, JSON, or PDF format
2. **Given** an export format is selected, **When** the download completes, **Then** the file contains all calculated metrics, query details, and summary statistics
3. **Given** a PDF report is generated, **When** the developer opens it, **Then** it includes visualizations, tables, and formatted metric explanations

---

### User Story 4 - Save and Load Previous Analyses (Priority: P3)

A developer wants to compare metrics across different versions of their RAG system by saving analysis results and loading them later.

**Why this priority**: Supports iterative development and A/B testing. Valuable but not critical for initial adoption.

**Independent Test**: Can be tested by calculating metrics, saving the analysis, closing the browser, returning later, and successfully loading the saved analysis with all data intact.

**Acceptance Scenarios**:

1. **Given** metrics have been calculated, **When** the developer clicks "Save Analysis", **Then** the system stores the dataset, metrics, and timestamp
2. **Given** previous analyses exist, **When** the developer opens the website, **Then** they see a list of saved analyses with dates and dataset names
3. **Given** a saved analysis is selected, **When** the developer clicks "Load", **Then** all metrics and visualizations are restored exactly as they were

---

### Edge Cases

- What happens when the uploaded CSV file has missing values in critical columns (queries, responses, or ground truth)?
- How does the system handle CSV files with incorrect column headers or unexpected data formats?
- What happens when a CSV file is too large (e.g., >10,000 rows or >50MB)?
- How does the system respond when ground truth data is ambiguous or multiple valid answers exist?
- What happens if a user tries to calculate metrics without uploading a file first?
- How does the system handle special characters, multilingual text, or unusual encodings in CSV data?
- What happens when a user navigates away during metric calculation?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST accept CSV file uploads with a maximum file size of 50MB
- **FR-002**: System MUST validate CSV files to ensure they contain required columns: query text, generated response, and ground truth answer
- **FR-003**: System MUST display clear error messages when CSV validation fails, specifying which columns are missing or incorrectly formatted
- **FR-004**: System MUST calculate standard RAG metrics including precision, recall, F1 score, and semantic similarity scores
- **FR-005**: System MUST display calculated metrics in both numerical and visual formats (charts, graphs)
- **FR-006**: System MUST provide explanations for each metric, describing what it measures and how to interpret the values
- **FR-007**: System MUST show a preview of uploaded CSV data (first 10 rows) before calculation
- **FR-008**: System MUST allow users to map CSV columns to required fields if column names don't match expected format
- **FR-009**: System MUST handle missing values by either skipping those rows or providing imputation options
- **FR-010**: System MUST display per-query metric breakdowns in addition to aggregate statistics
- **FR-011**: System MUST support exporting results in CSV, JSON, and PDF formats
- **FR-012**: System MUST use Carbon Design System components for all UI elements to ensure consistency
- **FR-013**: System MUST display the IBM Bob logo prominently on the page header for branding
- **FR-014**: System MUST be responsive and work on desktop browsers (minimum viewport width: 1024px)
- **FR-015**: System MUST provide visual feedback during file upload and metric calculation (progress indicators)
- **FR-016**: System MUST allow users to save analysis results locally (browser storage or downloadable file)
- **FR-017**: System MUST allow users to load previously saved analyses
- **FR-018**: System MUST display calculation time and dataset statistics (number of queries, average response length)

### Key Entities

- **RAG Dataset**: Represents uploaded data containing queries, generated responses, and ground truth answers. Attributes include dataset name, upload timestamp, row count, and column mappings.
- **Metric Result**: Represents calculated performance metrics for a dataset. Attributes include metric type (precision, recall, F1, semantic similarity), aggregate value, per-query values, and calculation timestamp.
- **Query Analysis**: Represents individual query-level analysis. Attributes include query text, generated response, ground truth answer, individual metric scores, and any identified issues.
- **Saved Analysis**: Represents a stored analysis session. Attributes include dataset snapshot, calculated metrics, timestamp, and user-provided name/description.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Developers can upload a CSV file and view calculated RAG metrics within 30 seconds for datasets up to 1,000 queries
- **SC-002**: System successfully processes and calculates metrics for 95% of properly formatted CSV files on first attempt
- **SC-003**: Users can identify their lowest-performing queries within 2 minutes of viewing results
- **SC-004**: 90% of users successfully complete the upload-calculate-view workflow without requiring help documentation
- **SC-005**: Exported reports contain all necessary information for sharing with team members (no need to access the website again)
- **SC-006**: System handles datasets with up to 5,000 queries without performance degradation (calculation completes within 2 minutes)
- **SC-007**: Users can compare metrics across different RAG system versions by loading saved analyses in under 10 seconds
- **SC-008**: Error messages enable users to fix CSV formatting issues without external help in 80% of cases

## Assumptions

- Developers using this tool have basic understanding of RAG systems and common evaluation metrics
- CSV files follow standard formatting conventions (comma-separated, UTF-8 encoding)
- Users have access to modern web browsers (Chrome, Firefox, Safari, Edge - latest 2 versions)
- Ground truth answers are provided in the CSV; the system does not generate or validate ground truth
- Semantic similarity calculations will use standard text similarity algorithms (cosine similarity, BLEU, ROUGE)
- Users are responsible for data privacy and security of uploaded CSV files
- The website will be a client-side application or have minimal backend processing
- Carbon Design System is compatible with the chosen web framework
- Users have datasets ready for evaluation (the tool does not help create test datasets)

## Dependencies

- Carbon Design System library and components must be available and compatible
- Text similarity calculation libraries or APIs for semantic metrics
- CSV parsing library that handles various CSV formats and encodings
- Chart/visualization library compatible with Carbon Design System
- Browser local storage API for saving analyses (or backend storage if implemented)

## Out of Scope

- Generating synthetic test data or ground truth answers
- Integration with specific RAG frameworks or LLM APIs
- Real-time monitoring of production RAG systems
- User authentication or multi-user collaboration features
- Advanced statistical analysis beyond standard RAG metrics
- Automated suggestions for improving RAG system performance
- Support for non-CSV data formats (JSON, XML, databases)
- Mobile device support (tablets and phones)
- Hosting or deployment infrastructure
