from flask import Flask, Blueprint, request, jsonify, render_template, session
import json

app = Flask(__name__)

atividade3_blueprint = Blueprint('atividade3', __name__, template_folder='templates', static_folder='static')

mock_username = "usuario"
mock_password = "senha123"
MAX_ATTEMPTS = 2 

@atividade3_blueprint.route('/')
def index():
    return render_template('autenticar.html')

@atividade3_blueprint.route('/authenticate', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if username != "":
        if password != "":
            if username == mock_username and password == mock_password:
                return jsonify({"message": "Bem-vindo, usuário!"}), 200
            else:
                return jsonify({"message": "Login inválido. Usuário ou senha incorretos."}), 401
        else:
            return jsonify({"message": "Preencha a senha corretamente"}), 401
    else:
        return jsonify({"message": "Preencha o usuario corretamente"}), 401


app.register_blueprint(atividade3_blueprint, url_prefix='/atividade3')

if __name__ == '__main__':
    app.run(debug=True)
