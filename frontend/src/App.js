import React, { useState, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';

function App() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
  fetch('http://127.0.0.1:5000/api/data') // Adjust the URL if needed
    .then((response) => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then((data) => setData(data.message))
    .catch((error) => {
      console.error('Fetch error:', error);
      setError(error.message);
    });
  }, []);

  if (error) return <div>Error: {error}</div>;

  return (
    // <h1>{data ? data : 'Loading...'}</h1>
    <div className="App">
      <ReactMarkdown>{data ? data : 'Loading...'}</ReactMarkdown>
    </div>
  );
}

export default App;
