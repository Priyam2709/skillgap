import { BrowserRouter as Router, Routes, Route }
from "react-router-dom";

import AuthPage from "./pages/AuthPage";
import HomePage from "./pages/Home";
import Dashboard from "./pages/Dashboard";
import ProtectedRoute from "./components/ProtectedRoute";

function App() {

  return (
    <Router>

      <Routes>

        <Route path="/" element={<AuthPage />} />

        <Route
          path="/home"
          element={
            <ProtectedRoute>
              <HomePage />
            </ProtectedRoute>
          }
        />

        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />

      </Routes>

    </Router>
  );
}

export default App;