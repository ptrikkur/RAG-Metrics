# Quickstart Guide: RAG Metrics Calculator Website

**Feature**: RAG Metrics Calculator Website  
**Branch**: `001-rag-metrics-website`  
**Date**: 2026-01-27

## Overview

This guide helps developers quickly set up and run the RAG Metrics Calculator application locally. The application consists of a React frontend (static site) and a Python FastAPI backend.

## Prerequisites

### Required Software

- **Node.js**: v18.0.0 or higher
- **npm**: v9.0.0 or higher (comes with Node.js)
- **Python**: 3.11 or higher
- **pip**: Latest version
- **Git**: For version control

### Verify Installation

```bash
node --version    # Should be v18.0.0+
npm --version     # Should be v9.0.0+
python --version  # Should be 3.11+
pip --version     # Should show latest
```

## Project Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd rag-metrics
git checkout 001-rag-metrics-website
```

### 2. Backend Setup

#### Install Python Dependencies

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### Backend Dependencies (requirements.txt)

```txt
fastapi==0.109.0
uvicorn[standard]==0.27.0
pydantic==2.5.3
pandas==2.1.4
numpy==1.26.3
scikit-learn==1.4.0
sentence-transformers==2.3.1
nltk==3.8.1
rouge-score==0.1.2
reportlab==4.0.9
python-multipart==0.0.6
```

#### Download NLTK Data (First Time Only)

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

#### Run Backend Server

```bash
# From backend directory
uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at: `http://localhost:8000`

API documentation: `http://localhost:8000/docs`

### 3. Frontend Setup

#### Install Node Dependencies

```bash
cd frontend

# Install dependencies
npm install
```

#### Frontend Dependencies (package.json)

```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.21.0",
    "@carbon/react": "^1.47.0",
    "@carbon/charts": "^1.13.0",
    "@carbon/charts-react": "^1.13.0",
    "papaparse": "^5.4.1",
    "axios": "^1.6.5"
  },
  "devDependencies": {
    "@types/react": "^18.2.48",
    "@types/react-dom": "^18.2.18",
    "@types/papaparse": "^5.3.14",
    "@vitejs/plugin-react": "^4.2.1",
    "typescript": "^5.3.3",
    "vite": "^5.0.11",
    "eslint": "^8.56.0",
    "prettier": "^3.1.1"
  }
}
```

#### Configure Environment Variables

Create `.env` file in frontend directory:

```bash
VITE_API_BASE_URL=http://localhost:8000
```

#### Run Frontend Development Server

```bash
# From frontend directory
npm run dev
```

Frontend will be available at: `http://localhost:5173`

## Quick Test

### 1. Prepare Test Data

Create a sample CSV file (`test_data.csv`):

```csv
question,generated_answer,correct_answer
What is the capital of France?,The capital of France is Paris.,Paris
What is 2+2?,The answer is 4.,4
Who wrote Romeo and Juliet?,William Shakespeare wrote Romeo and Juliet.,William Shakespeare
```

### 2. Test the Application

1. Open browser to `http://localhost:5173`
2. Click "Upload CSV" button
3. Select `test_data.csv`
4. Review the data preview
5. Click "Calculate Metrics"
6. View the results (should show high precision/recall for this simple data)
7. Try exporting results as CSV, JSON, or PDF

### 3. Verify Backend API

Test the health endpoint:

```bash
curl http://localhost:8000/health
```

Expected response:
```json
{
  "status": "healthy",
  "timestamp": "2026-01-27T12:00:00Z",
  "version": "1.0.0"
}
```

## Development Workflow

### Running Tests

#### Backend Tests

```bash
cd backend
pytest tests/ -v --cov=src
```

#### Frontend Tests

```bash
cd frontend
npm test
```

### Code Formatting

#### Backend (Python)

```bash
cd backend
black src/ tests/
isort src/ tests/
```

#### Frontend (TypeScript/React)

```bash
cd frontend
npm run format
npm run lint
```

### Building for Production

#### Backend

```bash
cd backend
# Backend runs directly with uvicorn, no build step needed
```

#### Frontend

```bash
cd frontend
npm run build
```

Build output will be in `frontend/dist/` directory.

## Project Structure

```
rag-metrics/
├── backend/
│   ├── src/
│   │   ├── api/
│   │   │   ├── routes/
│   │   │   │   ├── metrics.py
│   │   │   │   └── health.py
│   │   │   └── main.py
│   │   ├── services/
│   │   │   ├── csv_validator.py
│   │   │   ├── metrics_calculator.py
│   │   │   └── semantic_similarity.py
│   │   ├── models/
│   │   │   ├── dataset.py
│   │   │   └── metric_result.py
│   │   └── utils/
│   │       └── error_handlers.py
│   ├── tests/
│   ├── requirements.txt
│   └── pyproject.toml
│
├── frontend/
│   ├── public/
│   │   ├── index.html
│   │   └── assets/
│   │       └── ibm-bob-logo.svg
│   ├── src/
│   │   ├── components/
│   │   │   ├── FileUpload/
│   │   │   ├── MetricsDisplay/
│   │   │   ├── ResultsTable/
│   │   │   ├── DataPreview/
│   │   │   ├── ExportButton/
│   │   │   └── Header/
│   │   ├── pages/
│   │   │   ├── Home.tsx
│   │   │   ├── Results.tsx
│   │   │   └── SavedAnalyses.tsx
│   │   ├── services/
│   │   │   ├── api.ts
│   │   │   ├── csvParser.ts
│   │   │   └── storage.ts
│   │   ├── types/
│   │   │   ├── dataset.ts
│   │   │   └── metrics.ts
│   │   ├── utils/
│   │   │   └── formatters.ts
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── tests/
│   ├── package.json
│   ├── vite.config.ts
│   └── tsconfig.json
│
└── specs/
    └── 001-rag-metrics-website/
        ├── spec.md
        ├── plan.md
        ├── research.md
        ├── data-model.md
        ├── quickstart.md (this file)
        └── contracts/
            └── openapi.yaml
```

## Common Issues & Solutions

### Issue: Backend fails to start

**Solution**: Ensure virtual environment is activated and all dependencies are installed:
```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Issue: Frontend can't connect to backend

**Solution**: Check that:
1. Backend is running on port 8000
2. `.env` file has correct `VITE_API_BASE_URL`
3. CORS is configured in backend to allow frontend origin

### Issue: Semantic similarity calculation is slow

**Solution**: First run downloads the sentence-transformer model (~90MB). Subsequent runs will be faster. For development, you can use a smaller model in `backend/src/services/semantic_similarity.py`.

### Issue: CSV upload fails

**Solution**: Verify:
1. File size is under 50MB
2. File is valid CSV format
3. Required columns (query, response, groundTruth) exist

### Issue: PDF export not working

**Solution**: Ensure ReportLab is installed:
```bash
pip install reportlab==4.0.9
```

## Next Steps

1. **Read the Specification**: Review [`spec.md`](./spec.md) for feature requirements
2. **Review Data Model**: Check [`data-model.md`](./data-model.md) for entity definitions
3. **Explore API Contracts**: See [`contracts/openapi.yaml`](./contracts/openapi.yaml) for API details
4. **Run Tests**: Execute test suites to verify setup
5. **Start Development**: Begin implementing features according to the plan

## Useful Commands

### Backend

```bash
# Run server with auto-reload
uvicorn src.api.main:app --reload

# Run tests with coverage
pytest --cov=src --cov-report=html

# Format code
black src/ tests/
isort src/ tests/

# Type checking
mypy src/
```

### Frontend

```bash
# Development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Run tests
npm test

# Run tests with coverage
npm test -- --coverage

# Lint code
npm run lint

# Format code
npm run format
```

## Environment Variables

### Backend (.env)

```bash
# Optional: Set log level
LOG_LEVEL=INFO

# Optional: Set CORS origins
CORS_ORIGINS=http://localhost:5173,http://localhost:3000
```

### Frontend (.env)

```bash
# Required: Backend API URL
VITE_API_BASE_URL=http://localhost:8000

# Optional: Enable debug mode
VITE_DEBUG=true
```

## Performance Tips

1. **Use code splitting**: Frontend automatically splits code by route
2. **Enable caching**: Browser caches static assets automatically
3. **Optimize images**: Use optimized SVG for IBM Bob logo
4. **Lazy load charts**: Charts are loaded only when needed
5. **Batch API requests**: Process multiple queries in single request

## Security Notes

- No authentication required for MVP
- CORS configured for local development
- Input validation on both client and server
- File size limits enforced (50MB max)
- No data persistence on server (stateless)

## Support & Resources

- **API Documentation**: http://localhost:8000/docs
- **Carbon Design System**: https://carbondesignsystem.com/
- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **React Docs**: https://react.dev/
- **Vite Docs**: https://vitejs.dev/

## License

[Add license information here]

---

**Last Updated**: 2026-01-27  
**Version**: 1.0.0