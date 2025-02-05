from flask import Flask, Blueprint, request, jsonify, render_template, render_template_string
import json
import os

app = Flask(__name__)
atividade2_blueprint = Blueprint('atividade2', __name__, template_folder='templates', static_folder='static')

mock_username = "usuario"
mock_password = "senha123"

form_data_json = '''
{
    "title": "Formulário de Cadastro",
    "fields": [
        {"label": "Nome", "name": "nome", "type": "text"},
        {"label": "Email", "name": "email", "type": "email"},
        {"label": "Idade", "name": "idade", "type": "number"},
        {"label": "Senha", "name": "senha", "type": "password"}
    ]
}
'''
form_data = json.loads(form_data_json)

def generate_form_html(data):
    title = data.get("title", "Formulário")
    fields = data.get("fields", [])
    css = "{{ url_for('static', filename='css/style.css') }}"

    form_html = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="{css}">
        <title>{title}</title>
    </head>
    <body>
        <div class="container">
            <button onclick="window.location.href='./'" class="voltar">Voltar</button>
            <h1>{title}</h1>
            <div class="activity-list">
                <form onsubmit="submitForm(event)">
    """

    for field in fields:
        label = field.get("label", "Campo")
        name = field.get("name", "campo")
        field_type = field.get("type", "text")
        form_html += f"""
                    <label for="{name}">{label}</label>
                    <input type="{field_type}" id="{name}" name="{name}">
                    <br>
        """

    form_html += """
                    <button type="submit">Enviar</button>
                </form>
            </div>
        </div>
        <script src="{{ url_for('atividades.atividade2.static', filename='js/script01.js') }}"></script>
    </body>
    </html>
    """

    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    os.makedirs(template_dir, exist_ok=True)
    template_path = os.path.join(template_dir, "formulario.html")

    with open(template_path, "w", encoding="utf-8") as file:
        file.write(form_html)

    return form_html


@atividade2_blueprint.route('/')
def index():
    return render_template('index06.html')

@atividade2_blueprint.route('/telaLogin')
def telaLogin():
    return render_template('login.html')

@atividade2_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    print(username, password)

    if username == mock_username and password == mock_password:
        return "Bem-vindo, usuário!"
    else:
        return "Login inválido. Usuário ou senha incorretos."

@atividade2_blueprint.route('/formulario')
def formulario():
    generate_form_html(form_data) 
    return render_template('formulario.html') 

app.register_blueprint(atividade2_blueprint, url_prefix='/atividade2')