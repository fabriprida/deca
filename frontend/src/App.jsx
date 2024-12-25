import { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetch('/api/')
      .then((response) => response.json())
      .then((data) => setMessage(data.message))
      .catch((error) => console.error('Error:', error));
  }, []);

  return (
    <div className="App">
      <h1>Frontend con React y Vite</h1>
      <h1>hello</h1>
      <p>Mensaje del backend: {message}</p>
    </div>
  );
}

export default App;
