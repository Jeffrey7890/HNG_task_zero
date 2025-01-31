from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    data = {
            'email': 'jeffrey.ogechi@gmail.com',
            'current_datetime':datetime.utcnow().isoformat() + "Z",
            'github_url':'https://github.com/Jeffrey7890/HNG_task_zero'
            }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
