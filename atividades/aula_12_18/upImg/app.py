from flask import Flask, render_template, request, Blueprint
from datetime import datetime
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'atividades/aula_12_18/upImg/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

arquivos = []

atividadeUploadImg_blueprint = Blueprint('atividadeUploadImg', __name__, template_folder='templates', static_folder='static')

@atividadeUploadImg_blueprint.route('/', methods=['GET', 'POST'])
def uploadImagem():
    mensagem = None
    path_arquivo = None
    if request.method == 'POST':
        arquivo = request.files.get('arquivo')
        if arquivo and arquivo.filename:
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            caminho = os.path.join(app.config['UPLOAD_FOLDER'], f"{timestamp}_{arquivo.filename}")
            arquivo.save(caminho)
            arquivos.append({'nome': arquivo.filename, 'path': caminho, 'datetime': datetime.now()})
            mensagem = 'Upload realizado com sucesso!'
            path_arquivo = caminho
        else:
            mensagem = 'Falha no upload. Nenhum arquivo selecionado.'
    return render_template('uploadImagem.html', mensagem=mensagem, path_arquivo=path_arquivo)

app.register_blueprint(atividadeUploadImg_blueprint, url_prefix='/atividadeUploadImg')

if __name__ == '__main__':
    app.run(debug=True)
