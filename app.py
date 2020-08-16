from flask import Flask, render_template, request, jsonify
from DB import Database
from flask_cors import CORS

db = Database()

def format_result(error, data=None):
    result = {}
    if error:
        result['status'] = 'error'
        result['error'] = error
    else:
        result['status'] = 'success'
        result['data'] = data

    return result


app = Flask(__name__)

CORS(app)

@app.route('/')
def root():
    return "<h1>welcome to user service</h1>"


@app.route('/user/all')
def get_users():
    statement = f"select id, name, email from user"
    result = db.dcl(statement)
    return jsonify(result)


@app.route('/user/register', methods=["POST"])
def register_user():
    email = request.json.get('email')
    password = request.json.get('password')
    name = request.json.get('name')

    statement = f"insert into user (name, email, password) values ('{name}', '{email}', '{password}')"
    db.dml(statement)
    return format_result(None, "user registered")


@app.route('/user/login', methods=["POST"])
def login_user():
    email = request.json.get('email')
    password = request.json.get('password')

    statement = f"select id, name, email from user where email= '{email}' and password = '{password}'"
    result = db.dcl(statement)
    if len(result) == 0:
        return format_result("user not exist")
    else:
        user = result[0]
        return format_result(None, {
            "id": user[0],
            "name": {user[1]},
            "email": user[2]
        })


app.run(port=4000, host='0.0.0.0', debug=True)