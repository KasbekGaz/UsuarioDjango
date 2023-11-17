import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from "react-router-dom";



export function LoginView() {

    const navigate = useNavigate();

    const [userData, setUserData] = useState({
            username: '',
            password: '',
        });
    
        const handleChange = (e) => {
            setUserData({
                ...userData,
                [e.target.name]: e.target.value
            })
        };

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        try {
            // ! Realizar la solicitud de registro al backend
            const response = await axios.post('http://127.0.0.1:8000/login/', userData);
            console.log('Inicio de sesión exitoso. Token almacenado:', response.data.token);

            // Almacenar el token en el localStorage
            localStorage.setItem('token', response.data.token);

            navigate('/obras');

          } catch (error) {
            console.error('Error al iniciar sesion:', error);
          }
    
    };



    return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
        <div className="bg-white p-8 shadow-md rounded-md">
            <h2 className="text-2xl font-semibold mb-4">Inicio de Sesion</h2>
            <form onSubmit={handleSubmit}>
                <label className="block mb-2" >
                    Nombre de Usuario:
                    <input type="text" name="username" 
                    value={userData.username} 
                    onChange={handleChange} 
                    className="w-full border rounded-md py-2 px-3 mt-1"/>
                </label>
                <br />
                <label className="block mb-2" >
                    Contraseña:
                    <input type="password" name="password" value={userData.password} onChange={handleChange} className="w-full border rounded-md py-2 px-3 mt-1"/>
                </label>
                <br />
                <button type='submit' className="bg-green-500 text-white mb-2 py-2 px-6 rounded-md hover:bg-green-700"> Entrar </button>
                <br />
            </form>
        </div>
    </div>
    );
}

