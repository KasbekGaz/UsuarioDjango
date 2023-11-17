import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom'

const RegisterView = () => {

    const navigate = useNavigate();


    const [userData, setUserData] = useState({
        username: '',
        password: '',
        email: '',
        telefono: '',
        rol: 'Consul',
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
        const response = await axios.post('http://127.0.0.1:8000/register/', userData);
        console.log('Usuario registrado con éxito:', response.data);
    
        navigate('/login'); //! redirecciona a inicio de sesion
    
      } catch (error) {
        console.error('Error al registrar usuario:', error);
    
        if (error.response) {
          console.error('Respuesta del servidor:', error.response.data);
        }
      }
    };
    
    
    

    return (
        <div  className="min-h-screen flex items-center justify-center bg-gray-50">
          <div className="bg-white p-8 shadow-md rounded-md">
            <h2 className="text-2xl font-semibold mb-4" >Registro de Usuario</h2>
            <form onSubmit={handleSubmit}>
              <label className="block mb-2">
                Nombre de Usuario:
                <input 
                type="text" 
                name="username" 
                value={userData.username} 
                onChange={handleChange} 
                className="w-full border rounded-md py-2 px-3 mt-1"
                />
              </label>
              <br />
              <label className="block mb-2">
                Contraseña:
                <input type="password" name="password" value={userData.password} onChange={handleChange} className="w-full border rounded-md py-2 px-3 mt-1" />
              </label>
              <br />
              <label className="block mb-2">
                Email:
                <input type="email" name="email" value={userData.email} onChange={handleChange} className="w-full border rounded-md py-2 px-3 mt-1" />
              </label>
              <br />
              <label className="block mb-2">
                Teléfono:
                <input type="text" name="telefono" value={userData.telefono} onChange={handleChange} className="w-full border rounded-md py-2 px-3 mt-1"/>
              </label>
              <br />
              <label className="block mb-2">
                Rol:
                <select 
                name="rol" 
                value={userData.rol} 
                onChange={handleChange} className="w-full border rounded-md py-2 px-3 mt-1">
                  <option value="Admin">Admin</option>
                  <option value="Consul">Consul</option>
                </select>
              </label>
              <br />
              <button type="submit" className="bg-green-500 text-white py-2 px-4 rounded-md hover:bg-green-700">Registrar</button>
            </form>
          </div>
        </div>
      );




};

export default RegisterView;