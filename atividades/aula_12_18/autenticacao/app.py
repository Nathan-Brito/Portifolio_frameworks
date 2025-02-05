from flask import Flask, Blueprint, render_template, request, redirect, url_for
from datetime import datetime
import os

app = Flask(__name__)

usuarios = {'admin': '1234'}
tentativas = []

auth_blueprint = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

@auth_blueprint.route('/', methods=['GET', 'POST'])
def login_preprova():
    mensagem = None
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        if usuario in usuarios and usuarios[usuario] == senha:
            tentativas.append({'usuario': usuario, 'status': 'Sucesso', 'datetime': datetime.now()})
            return redirect(url_for('.painel', usuario=usuario))
        else:
            tentativas.append({'usuario': usuario, 'status': 'Falha', 'datetime': datetime.now()})
            mensagem = 'Usuário ou senha incorretos.'
    return render_template('loginPreProva.html', mensagem=mensagem)

@auth_blueprint.route('/painel')
def painel():
    usuario = request.args.get('usuario')
    if not usuario or usuario not in usuarios:
        return redirect(url_for('auth.login_preprova'))
    return render_template('painel.html', usuario=usuario)

@auth_blueprint.route('/logout')
def logout():
    return redirect(url_for('.login_preprova'))

app.register_blueprint(auth_blueprint, url_prefix='/auth')