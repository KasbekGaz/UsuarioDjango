import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from "react-router-dom";

const ObraForm = () => {
    const navigate = useNavigate();


  const [obraData, setObraData] = useState({
    nombre: '',
    localidad: '',
    municipio: '',
    dependencia: '',
    fecha: '',
    p_inicial: 0,
  });

  const [error, setError] = useState(null);

  const handleInputChange = (e) => {
    setObraData({
      ...obraData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const token = localStorage.getItem('token');

      const response = await axios.post('http://127.0.0.1:8000/v1/api/obras/', obraData, {
        headers: {
          Authorization: `Token ${token}`,
        },
      });

      console.log('Obra registrada:', response.data)

      navigate('/Obras')

      // Limpiar el formulario después de enviar la obra
      setObraData({
        nombre: '',
        localidad: '',
        municipio: '',
        dependencia: '',
        fecha: '',
        p_inicial: 0,
      });

      // Puedes agregar un mensaje de éxito o redirección aquí
     
    } catch (error) {
      console.error('Error al agregar la nueva obra:', error.response);
      setError('Error al registrar la nueva obra. Por favor, intenta de nuevo más tarde.');
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h2 className="text-2xl font-semibold mb-4">Registro de Nueva Obra</h2>
      {error && <p className="text-red-500">{error}</p>}

      <form onSubmit={handleSubmit}>
        <label className="block mb-2">
          Nombre:
          <input
            type="text"
            name="nombre"
            value={obraData.nombre}
            onChange={handleInputChange}
            className="w-full border rounded-md py-2 px-3 mt-1"
          />
        </label>
        <br />
        <label className="block mb-2">
          Localidad:
          <input
            type="text"
            name="localidad"
            value={obraData.localidad}
            onChange={handleInputChange}
            className="w-full border rounded-md py-2 px-3 mt-1"
          />
        </label>
        <br />
        <label className="block mb-2">
          Municipio:
          <input
            type="text"
            name="municipio"
            value={obraData.municipio}
            onChange={handleInputChange}
            className="w-full border rounded-md py-2 px-3 mt-1"
          />
        </label>
        <br />
        <label className="block mb-2">
          Dependencia:
          <input
            type="text"
            name="dependencia"
            value={obraData.dependencia}
            onChange={handleInputChange}
            className="w-full border rounded-md py-2 px-3 mt-1"
          />
        </label>
        <br />
        <label className="block mb-2">
          Fecha:
          <input
            type="date"
            name="fecha"
            value={obraData.fecha}
            onChange={handleInputChange}
            className="w-full border rounded-md py-2 px-3 mt-1"
          />
        </label>
        
        <button type="submit" className="bg-blue-500 text-white py-2 px-4 rounded-md mt-4">
          Registrar Obra
        </button>
      </form>
    </div>
  );
};

export default ObraForm;
