from flask import Flask, jsonify

app = Flask(__name__)

people = [
    {"id": 1, "name": "Alice", "age": 24},
    {"id": 2, "name": "Bob", "age": 40}
]

@app.route('/people', methods=['GET'])
def get_people():
    return jsonify(people)

if __name__ == '__main__':
    app.run(debug=True)