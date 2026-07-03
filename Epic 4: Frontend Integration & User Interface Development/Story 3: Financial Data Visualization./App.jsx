import { BrowserRouter, Routes, Route } from "react-router-dom";

import Dashboard from "./components/Dashboard";
import FinancialHealth from "./components/FinancialHealth";
import SettlementPredictor from "./components/SettlementPredictor";
import NegotiationEmail from "./components/NegotiationEmail";
import KnowYourRights from "./components/KnowYourRights";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/financial-health" element={<FinancialHealth />} />
        <Route path="/settlement" element={<SettlementPredictor />} />
        <Route path="/email" element={<NegotiationEmail />} />
        <Route path="/rights" element={<KnowYourRights />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
