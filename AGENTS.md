# rag-metrics Development Guidelines

Auto-generated from all feature plans. Last updated: 2026-01-27

## Active Technologies

### Frontend
- React 18+ with TypeScript
- Carbon Design System (@carbon/react)
- Vite (build tool)
- Carbon Charts for visualizations
- Papa Parse for CSV parsing

### Backend
- Python 3.11+
- FastAPI (REST API framework)
- pandas, numpy (data processing)
- scikit-learn (metrics calculation)
- sentence-transformers (semantic similarity)
- ReportLab (PDF generation)

### Storage
- Browser localStorage for saved analyses (client-side)
- No persistent backend database (stateless API)

## Project Structure

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
├── package.json
├── vite.config.ts
└── tsconfig.json
```

## Commands

### Backend
```bash
# Setup
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Run development server
uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000

# Run tests
pytest tests/ -v --cov=src

# Format code
black src/ tests/
isort src/ tests/
```

### Frontend
```bash
# Setup
cd frontend
npm install

# Run development server
npm run dev

# Build for production
npm run build

# Run tests
npm test

# Format code
npm run format
npm run lint
```

## Code Style

### Frontend (TypeScript/React)
- Use TypeScript for type safety
- Follow Carbon Design System patterns
- Use functional components with hooks
- ESLint + Prettier for formatting
- Component naming: PascalCase
- File naming: PascalCase for components, camelCase for utilities

### Backend (Python)
- Follow PEP 8 style guide
- Use Black for formatting (line length: 88)
- Use isort for import sorting
- Type hints required for all functions
- Docstrings for all public functions (Google style)
- Function naming: snake_case

## Recent Changes

- 001-rag-metrics-website: Added

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
