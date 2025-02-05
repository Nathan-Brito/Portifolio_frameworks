from flask import Flask, render_template
from atividades.app import atividades_blueprint
from aulas.app import aulas_blueprint
from flask_scss import Scss
import os

app = Flask(__name__)

app.register_blueprint(atividades_blueprint, url_prefix='/atividades')
app.register_blueprint(aulas_blueprint, url_prefix='/aulas')

app.config['SCSS_ASSET_DIR'] = 'static/sass'  
app.config['SCSS_STATIC_DIR'] = 'static/css'  

Scss(app)
@app.route('/')
def index():
    return render_template('index.html') 

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) 
    app.run(host='0.0.0.0', port=port, debug=True) 
