import os
from flask import Flask, jsonify, send_from_directory, Response
from flask_cors import CORS
from typing import Union
from pathlib import Path

# Define base and build paths
base_path = Path(__file__).resolve().parent
build_path = base_path / 'frontend' / 'build'

# Create Flask app
app = Flask(__name__, static_folder=str(build_path))
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data() -> Response:
    return jsonify({'message': 'Hello from Flask!'})

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
