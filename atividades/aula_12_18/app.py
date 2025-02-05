from flask import Blueprint, render_template
from atividades.aula_12_18.miniBlog.app import atividadeBlog_blueprint
from atividades.aula_12_18.autenticacao.app import auth_blueprint
from atividades.aula_12_18.upImg.app import atividadeUploadImg_blueprint

atividade4_blueprint = Blueprint('atividade4', __name__, template_folder='templates')

atividade4_blueprint.register_blueprint(atividadeBlog_blueprint, url_prefix='/atividadeBlog')
atividade4_blueprint.register_blueprint(auth_blueprint, url_prefix='/auth')
atividade4_blueprint.register_blueprint(atividadeUploadImg_blueprint, url_prefix='/atividadeUploadImg')


@atividade4_blueprint.route('/')
def atividade4():
    return render_template('preProva.html')