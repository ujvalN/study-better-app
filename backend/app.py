from flask import Flask, jsonify, send_from_directory, Response, request
from flask_cors import CORS
from typing import Union
from pathlib import Path
from response import main

# Define base and build paths
base_path = Path(__file__).resolve().parent
build_path = base_path / 'frontend' / 'build'

# Create Flask app
app = Flask(__name__, static_folder=str(build_path))
CORS(app)

# Sends the response to frontend.
@app.route('/api/data', methods=['GET'])
def get_data() -> Response:
    course = request.args.get('course', default='AP Physics 1')
    n_questions = request.args.get('n_questions', default='8')
    n_flashcards = request.args.get('n_flashcards', default='6')
    topics = request.args.get('topics', default='').split(',')
    complexity = request.args.get('complexity', default='easy')

    response = main(course=course, n_questions=n_questions, n_flashcards=n_flashcards, topics=topics, complexity=complexity)
    return jsonify({'message': response})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path: Union[str, None]) -> Response:
    static_folder = str(app.static_folder)
    if path and (Path(static_folder) / path).exists():
        return send_from_directory(static_folder, path)
    else:
        return send_from_directory(static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
