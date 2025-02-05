from flask import Blueprint, render_template
from atividades.aula_10_30.app import atividade1_blueprint
from atividades.aula_11_06.app import atividade2_blueprint
from atividades.aula_11_13.app import atividade3_blueprint
from atividades.aula_12_18.app import atividade4_blueprint
from atividades.prova.app import prova_blueprint

atividades_blueprint = Blueprint('atividades', __name__, template_folder='static/templates')

atividades_blueprint.register_blueprint(atividade1_blueprint, url_prefix='/aula_10_30')
atividades_blueprint.register_blueprint(atividade2_blueprint, url_prefix='/aula_11_06')
atividades_blueprint.register_blueprint(atividade3_blueprint, url_prefix='/aula_11_13')
atividades_blueprint.register_blueprint(atividade4_blueprint, url_prefix='/aula_12_18')
atividades_blueprint.register_blueprint(prova_blueprint, url_prefix='/prova')

@atividades_blueprint.route('/')
def atividades_home():
    return render_template('atividades.html')
