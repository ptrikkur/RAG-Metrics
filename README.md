# RAG Metrics Calculator

A web application for calculating and analyzing RAG (Retrieval-Augmented Generation) system performance metrics.

## Features

- 📊 **CSV Upload**: Upload evaluation data containing queries, responses, and ground truth
- 📈 **Metrics Calculation**: Calculate precision, recall, F1 score, and semantic similarity
- 📉 **Detailed Analysis**: View per-query performance breakdowns
- 💾 **Save & Export**: Save analyses and export results in CSV, JSON, or PDF formats
- 🎨 **Modern UI**: Built with IBM Carbon Design System

## Tech Stack

### Frontend
- React 18+ with TypeScript
- Carbon Design System
- Vite (build tool)
- React Router for navigation

### Backend
- Python 3.11+
- FastAPI (REST API)
- pandas & numpy (data processing)
- scikit-learn (metrics calculation)
- sentence-transformers (semantic similarity)

## Quick Start

### Prerequisites

- Node.js v18.0.0+
- Python 3.11+
- npm v9.0.0+

### Frontend Setup

```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```

Frontend will be available at `http://localhost:5173`

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000
```

Backend API will be available at `http://localhost:8000`
API documentation at `http://localhost:8000/docs`

## Project Structure

```
rag-metrics/
├── backend/              # Python FastAPI backend
│   ├── src/
│   │   ├── api/         # API routes and main app
│   │   ├── models/      # Pydantic data models
│   │   ├── services/    # Business logic
│   │   └── utils/       # Utilities
│   └── tests/           # Backend tests
├── frontend/            # React TypeScript frontend
│   ├── src/
│   │   ├── components/  # React components
│   │   ├── pages/       # Page components
│   │   ├── services/    # API client & utilities
│   │   └── types/       # TypeScript types
│   └── tests/           # Frontend tests
└── specs/               # Feature specifications and planning docs
```

## Documentation

- [Feature Specification](specs/001-rag-metrics-website/spec.md)
- [Implementation Plan](specs/001-rag-metrics-website/plan.md)
- [API Contracts](specs/001-rag-metrics-website/contracts/openapi.yaml)
- [Data Model](specs/001-rag-metrics-website/data-model.md)
- [Frontend Quickstart](QUICKSTART-FRONTEND.md)

## Development Status

### ✅ Completed (Phase 1 & 2)
- Project structure and configuration
- Backend API foundation with FastAPI
- Frontend React app with routing
- IBM Bob branding and UI framework
- Base models and error handling

### 🚧 In Progress (Phase 3 - MVP)
- CSV file upload and validation
- Metrics calculation engine
- Results visualization
- Data preview component

### 📋 Planned
- Per-query detailed breakdowns (Phase 4)
- Export functionality (Phase 5)
- Save/load analyses (Phase 6)
- Advanced metrics (semantic similarity, BLEU, ROUGE)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

[Add your license here]

## Contact

[Add contact information]

---

**Built with ❤️ using IBM Carbon Design System**