import React, { useState, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import './App.css';  // CSS file for styling

function App() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [formData, setFormData] = useState({
    course: '',
    n_questions: '',
    n_flashcards: '',
    topics: '',
    complexity: 'easy',
  });

  // Handle form input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevFormData) => ({
      ...prevFormData,
      [name]: value,
    }));
  };

  const handleGenerate = () => {
    // Fetch data from backend after submitting the form
    fetch(`http://127.0.0.1:5000/api/data?course=${formData.course}&n_questions=${formData.n_questions}&n_flashcards=${formData.n_flashcards}&topics=${formData.topics}&complexity=${formData.complexity}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => {
        if (data && data.message) {
          setData(data.message);
        } else {
          console.error("Invalid response format", data);
          setError("Invalid response format");
        }
      })
      .catch((error) => {
        console.error('Fetch error:', error.message);
        setError(error.message);
      });
  };

  if (error) return <div>Error: {error}</div>;

  return (
    <div className="App">
      <h1>Study Material Generator</h1>
      <div className="form-container">
        <input
          type="text"
          name="course"
          placeholder="Course (e.g. AP Physics 1)"
          value={formData.course}
          onChange={handleChange}
        />
        <input
          type="number"
          name="n_questions"
          placeholder="Number of Questions"
          value={formData.n_questions}
          onChange={handleChange}
        />
        <input
          type="number"
          name="n_flashcards"
          placeholder="Number of Flashcards"
          value={formData.n_flashcards}
          onChange={handleChange}
        />
        <input
          type="text"
          name="topics"
          placeholder="Topics (comma-separated)"
          value={formData.topics}
          onChange={handleChange}
        />
        <select
          name="complexity"
          value={formData.complexity}
          onChange={handleChange}
        >
          <option value="easy">Easy</option>
          <option value="medium">Medium</option>
          <option value="hard">Hard</option>
        </select>
        <button onClick={handleGenerate} className="generate-btn">
          Generate Study Materials
        </button>
      </div>

      <div className="buttons-container">
        <button className="quiz-btn">Quiz</button>
        <button className="flashcards-btn">Flashcards</button>
        <button className="summary-btn">Summary</button>
      </div>

      {/* Render study materials as markdown */}
      <div className="output">
        <ReactMarkdown>{data ? data : 'Loading...'}</ReactMarkdown>
      </div>
    </div>
  );
}

export default App;