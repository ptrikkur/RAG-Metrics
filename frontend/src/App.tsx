import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Theme } from '@carbon/react';
import Header from './components/Header/Header';
import Home from './pages/Home';
import Results from './pages/Results';
import SavedAnalyses from './pages/SavedAnalyses';
import './App.css';

function App() {
  return (
    <Theme theme="white">
      <Router>
        <div className="app">
          <Header />
          <main className="app-content">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/results" element={<Results />} />
              <Route path="/saved" element={<SavedAnalyses />} />
            </Routes>
          </main>
        </div>
      </Router>
    </Theme>
  );
}

export default App;

// Made with Bob
