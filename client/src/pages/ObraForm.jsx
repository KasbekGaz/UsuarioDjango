import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from "react-router-dom";
import  ObraList  from "../components/ObraList";

const ObraForm = () => {
    //const navigate = useNavigate();


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

      //navigate('/Obras')

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
    <div className="flex items-center bg-slate-700">
      <div className="bg-blue p-8 mx-10 my-10 shadow-md rounded-md text-white bg-gradient-to-r from-blue-500 justify-left">
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
              className="w-full border rounded-md py-2 px-3 mt-1 text-black"
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
              className="w-full border rounded-md py-2 px-3 mt-1 text-black"
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
              className="w-full border rounded-md py-2 px-3 mt-1 text-black"
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
              className="w-full border rounded-md py-2 px-3 mt-1 text-black"
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
              className="w-full border rounded-md py-2 px-3 mt-1 text-black"
            />
          </label>
          <br />
          <label className="block mb-2">
            Presupuesto Inicial:
            <div className="relative mt-2 rounded-md shadow-sm">
              <div className="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
                <span className="text-gray-800 sm:text-sm">$</span>
              </div>
              <input
                type="text"
                name="p_inicial"
                value={obraData.p_inicial}
                onChange={handleInputChange}
                className="block w-full rounded-md border-0 py-1.5 pl-7 pr-20 text-black ring-1 ring-inset ring-gray-300 placeholder:text-gray-800 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                placeholder="0.00"
              />
            </div>
          </label>
          
          <button type="submit" className="bg-yellow-500 text-white py-2 px-4 rounded-md mt-4">
            Registrar Obra
          </button>
        </form>
        </div>

        <div >
          <ObraList />
        </div>
      
    </div>

  );
};

export default ObraForm;


