import "./App.css";
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Layout from "./pages/Layout";
import Food from "./pages/Food";
import Recommendation from "./pages/Recommendation";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="/food/:id" element={<Food />} />
          <Route path="/recommendation/:uid" element={<Recommendation />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
