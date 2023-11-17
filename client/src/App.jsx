import React from "react";
import { BrowserRouter, Routes, Route, Navigate} from 'react-router-dom'
import RegisterView from "./pages/RegisterView";
import { LoginView } from "./pages/LoginView";
import ObraList from "./components/ObraList";
import  ObraForm  from "./pages/ObraForm";

function App() {
  return(
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to ="/login"/>} />
        <Route path="/register" element={<RegisterView/>} />
        <Route path="/login" element={<LoginView/>} />
        <Route path="/obras" element={<ObraList/>} />
        <Route path="/create-obra" element={<ObraForm/>} />
      </Routes>
    </BrowserRouter>


  );
}


export default App
