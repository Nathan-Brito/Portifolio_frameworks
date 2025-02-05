from flask import Blueprint, render_template

atividade1_blueprint = Blueprint('atividade1', __name__, template_folder='templates', static_folder='static')

@atividade1_blueprint.route('/atv01')
@atividade1_blueprint.route('/atv01/')
def index01():
    return render_template('index01.html')

@atividade1_blueprint.route('/atv02')
@atividade1_blueprint.route('/atv02/')
def index02():
    return render_template('index02.html')

@atividade1_blueprint.route('/atv03')
@atividade1_blueprint.route('/atv03/')
def index03():
    return render_template('index03.html')

@atividade1_blueprint.route('/')
@atividade1_blueprint.route('/atv04')
@atividade1_blueprint.route('/atv04/')
def index04():
    return render_template('index04.html')

@atividade1_blueprint.route('/atv05')
@atividade1_blueprint.route('/atv05/')
def index05():
    return render_template('index05.html')

@atividade1_blueprint.route('/atv05/nathan')
def curriculo01():
    return render_template('atv05/curriculo01.html')

@atividade1_blueprint.route('/atv05/isabelle')
def curriculo02():
    return render_template('atv05/curriculo02.html')

@atividade1_blueprint.route('/atv05/caio')
def curriculo03():
    return render_template('atv05/curriculo03.html')

@atividade1_blueprint.route('/atv05/franciele')
def curriculo04():
    return render_template('atv05/curriculo04.html')

@atividade1_blueprint.route('/atv05/vinicius')
def curriculo05():
    return render_template('atv05/curriculo05.html')

@atividade1_blueprint.route('/atv05/thalita')
def curriculo06():
    return render_template('atv05/curriculo06.html')