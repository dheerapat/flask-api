from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/super_simple')
def super_simple():
    return jsonify(message="Hello from planetary API"), 200 #return json with key 'message'

@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message="Sorry, " + name + ", you are not old enough"), 401 #unauthorize
    else:
        return jsonify(message="Welcome, " + name)

@app.route('/url_variable/<string:name>/<int:age>')
def url_variable(name: str,age: int):
    if age < 18:
        return jsonify(message="Sorry, " + name + ", you are not old enough"), 401 #unauthorize
    else:
        return jsonify(message="Welcome, " + name)