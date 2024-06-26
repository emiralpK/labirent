from flask import Flask, jsonify, send_from_directory
from maze_generator import generate_and_solve

app = Flask(__name__)

@app.route('/maze')
def maze():
    maze, solution = generate_and_solve()
    return jsonify({'maze': maze, 'solution': solution})

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
