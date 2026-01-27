# Quick Start Guide: Running the Frontend

This guide will help you run the RAG Metrics Calculator frontend application.

## Prerequisites

- Node.js v18.0.0 or higher
- npm v9.0.0 or higher

Verify your installation:
```bash
node --version
npm --version
```

## Step-by-Step Instructions

### 1. Navigate to Frontend Directory

```bash
cd frontend
```

### 2. Install Dependencies

This will install React, TypeScript, Carbon Design System, and all other required packages:

```bash
npm install
```

**Note**: This may take 2-3 minutes depending on your internet connection.

### 3. Create Environment File

Copy the example environment file:

```bash
cp .env.example .env
```

The `.env` file should contain:
```
VITE_API_BASE_URL=http://localhost:8000
VITE_DEBUG=false
VITE_ENABLE_ANALYTICS=false
```

### 4. Start the Development Server

```bash
npm run dev
```

You should see output similar to:
```
  VITE v5.0.11  ready in 500 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h to show help
```

### 5. Open in Browser

Open your web browser and navigate to:
```
http://localhost:5173
```

## What You'll See

The application will display:
- **Header**: IBM Bob logo and "RAG Metrics Calculator" title
- **Navigation**: Links to "Home" and "Saved Analyses"
- **Home Page**: Welcome message with placeholder text

## Current Status

✅ **Working**:
- Application structure and routing
- Header with IBM Bob logo
- Navigation between pages
- Carbon Design System styling

⏳ **Coming Next** (Phase 3 - User Story 1):
- File upload functionality
- CSV validation
- Metrics calculation
- Results visualization

## Troubleshooting

### Port Already in Use

If port 5173 is already in use, Vite will automatically try the next available port (5174, 5175, etc.).

### Module Not Found Errors

If you see module errors, ensure all dependencies are installed:
```bash
npm install
```

### TypeScript Errors

TypeScript errors in the IDE are normal before dependencies are installed. They should disappear after running `npm install`.

### Cannot Find '@carbon/react'

Make sure you're in the `frontend` directory and have run `npm install`.

## Development Commands

```bash
# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Run linter
npm run lint

# Format code
npm run format
```

## Next Steps

1. **Explore the UI**: Navigate between Home and Saved Analyses pages
2. **Check the Code**: Review the component structure in `src/`
3. **Start Backend**: Follow backend setup to enable API functionality
4. **Continue Development**: Implement Phase 3 tasks for full functionality

## File Structure

```
frontend/
├── public/
│   ├── index.html          # HTML entry point
│   └── assets/
│       └── ibm-bob-logo.svg # IBM Bob logo
├── src/
│   ├── components/
│   │   └── Header/         # Header component with logo
│   ├── pages/
│   │   ├── Home.tsx        # Home page
│   │   ├── Results.tsx     # Results page (placeholder)
│   │   └── SavedAnalyses.tsx # Saved analyses page (placeholder)
│   ├── App.tsx             # Main app component with routing
│   ├── main.tsx            # React entry point
│   ├── index.css           # Global styles with Carbon
│   └── App.css             # App-specific styles
├── package.json            # Dependencies and scripts
├── vite.config.ts          # Vite configuration
└── tsconfig.json           # TypeScript configuration
```

## Support

For issues or questions:
1. Check the main README.md
2. Review the specification in `specs/001-rag-metrics-website/spec.md`
3. Check the implementation plan in `specs/001-rag-metrics-website/plan.md`

---

**Last Updated**: 2026-01-27