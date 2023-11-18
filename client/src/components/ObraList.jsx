import React, { useState, useEffect } from 'react';
import axios from 'axios';

export function ObraList () {
  const [obras, setObras] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchObras = async () => {
      try {
        const token = localStorage.getItem('token');
        console.log('Token enviado: ', token);

        const response = await axios.get('http://127.0.0.1:8000/v1/api/obras/', {
          headers: {
            Authorization: `Token ${token}`,
          },
        });

        setObras(response.data);
      } catch (error) {
        console.error('Error al obtener la lista de obras:', error.response);
        setError('Error al cargar la lista de obras. Por favor, intenta de nuevo más tarde. Puede que no haya inicidado sesion');
      } finally {
        setLoading(false);
      }
    };

    fetchObras();
  }, []);

  if (loading) {
    return <p>Cargando obras...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

  return (
    <div className="bg-blue p-8 mx-10 my-10 shadow-md rounded-md text-white justify-right">
      <div className="container mx-auto p-4">
      <h2 className="text-2xl font-semibold mb-4">Lista de Obras Registradas</h2>
      
      <ul className="list-disc pl-4">
        {obras.map((obra) => (
          <li key={obra.id} className="mb-2">
            <strong>{obra.nombre}</strong> - {obra.localidad}, {obra.municipio} ({obra.dependencia}) - Fecha: {obra.fecha} - Presupuesto: {obra.p_inicial}
          </li>
        ))}
      </ul>
    </div>
    </div>
  );
};

export default ObraList;