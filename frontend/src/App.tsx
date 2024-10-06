import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './pages/Login'; 
import './App.css';
import Verification from './pages/Verification';
import Authorizations from './pages/Authorizations';
import AuthorizationFail from './pages/AuthorizationFail';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />}/>
        <Route path="/success" element={<Verification />}/>
        <Route path="/auth" element={<Authorizations />}/>
        <Route path="/authfail" element={<AuthorizationFail />}/>
      </Routes>
    </Router>
  );
}

export default App;
