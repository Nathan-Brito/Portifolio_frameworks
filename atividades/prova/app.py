from flask import Flask, request, render_template, url_for, redirect, Blueprint

prova_blueprint = Blueprint('prova', __name__, template_folder='templates', static_folder='static')


faturas = [
    {"id": 1, "detalhes": "João Silva", "valor": "150.75", "data_status": "Paga"},
    {"id": 2, "detalhes": "Maria Oliveira", "valor": "300.0", "data_status": "Pendente"}
]
def gerar_id():
    return (max(fatura['id'] for fatura in faturas ) +1 if faturas else 1 )

@prova_blueprint.route('/')
def index():
    faturas_ordenadas = sorted(faturas, key=lambda x : x['data_status'])
    return render_template('homepage.html', faturas=faturas_ordenadas)

@prova_blueprint.route('/excluir/<int:id>', endpoint='excluir')
def excluir(id):
    global faturas
    faturas = [fatura for fatura in faturas if fatura['id'] != id]
    return redirect(url_for('atividades.prova.index'))

@prova_blueprint.route('/adicionar', methods = ['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        detalhes = request.form["detalhes"]
        valor = request.form["valor"]
        data_status = request.form["data_status"]

        nova_fatura = {
            "id": gerar_id(),
            "detalhes": detalhes,
            "valor": valor,
            "data_status": data_status
        }
        faturas.append(nova_fatura)
        return redirect(url_for('atividades.prova.index'))
    return render_template('adicionarFatura.html')