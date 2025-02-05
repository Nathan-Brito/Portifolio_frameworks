import os
from flask import Blueprint, render_template

aulas_blueprint = Blueprint('aulas', __name__, template_folder='templates')

def get_file_content(folder, filename='anotacoes.txt'):
    path = os.path.join(os.path.dirname(__file__), folder, filename)
    content = "Arquivo não encontrado."
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
    
    activity_link = f"/atividades/{folder}" 

    return content, activity_link 

@aulas_blueprint.route('/')
def aulas_home():
    return render_template('aulas.html')

@aulas_blueprint.route('/aula_10_16/')
def aula_10_16():
    annotations, activity_link = get_file_content('aula_10_16')
    return render_template('anotacoes.html', annotations=annotations, activity_link="")

@aulas_blueprint.route('/aula_10_23/')
def aula_10_23():
    annotations, activity_link = get_file_content('aula_10_23')
    return render_template('anotacoes.html', annotations=annotations, activity_link="")

@aulas_blueprint.route('/aula_10_30/')
def aula_10_30():
    annotations, activity_link = get_file_content('aula_10_30')
    return render_template('anotacoes.html', annotations=annotations, activity_link=activity_link)

@aulas_blueprint.route('/aula_11_06/')
def aula_11_06():
    annotations, activity_link = get_file_content('aula_11_06')
    return render_template('anotacoes.html', annotations=annotations, activity_link=activity_link)

@aulas_blueprint.route('/aula_11_13/')
def aula_11_13():
    annotations, activity_link = get_file_content('aula_11_13')
    return render_template('anotacoes.html', annotations=annotations, activity_link=activity_link)

@aulas_blueprint.route('/aula_12_18/')
def aula_12_18():
    annotations, activity_link = get_file_content('aula_12_18')
    return render_template('anotacoes.html', annotations=annotations, activity_link=activity_link)

@aulas_blueprint.route('/prova/')
def prova():
    annotations, activity_link = get_file_content('prova')
    return render_template('anotacoes.html', annotations=annotations, activity_link=activity_link)
