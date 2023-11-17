import React from "react";
import { BrowserRouter, Routes, Route, Navigate} from 'react-router-dom'
import RegisterView from "./pages/RegisterView";
import { LoginView } from "./pages/LoginView"

function App() {
  return(
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to ="/login"/>} />
        <Route path="/register" element={<RegisterView/>} />
        <Route path="/login" element={<LoginView/>} />
      </Routes>
    </BrowserRouter>


  );
}


export default App
