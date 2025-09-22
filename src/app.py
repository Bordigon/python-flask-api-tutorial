from flask import Flask, jsonify, request
app = Flask(__name__)

todos:list = [{"label":"My first task", "done":False, "id":1},{"label":"My second task", "done":False, "id":2},{"label":"My third task", "done":False, "id":3}]

@app.route("/todos", methods = ['GET'])  # Aquí definimos el primer path de la API: GET /
def hello_world():  # Este método se llamará cuando el cliente haga el request
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    request_body["id"] = len(todos)+1
    print("Incoming request with the following body", request_body)
    print(request_body["id"])
    todos.append(request_body)
    return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    del todos[position-1]
    return jsonify(todos)


# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)