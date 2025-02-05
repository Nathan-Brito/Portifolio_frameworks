from flask import Flask, Blueprint, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

posts = []

atividadeBlog_blueprint = Blueprint('atividadeBlog', __name__, template_folder='templates', static_folder='static')

@atividadeBlog_blueprint.route('/')
def blog():
    sorted_posts = sorted(posts, key=lambda x: x['datetime'], reverse=True)
    return render_template('blog.html', posts=sorted_posts)

@atividadeBlog_blueprint.route('/add', methods=['POST'])
def add_post():
    content = request.form.get('content')
    if content:
        posts.append({
            'content': content,
            'datetime': datetime.now()
        })
    return redirect(url_for('atividades.atividade4.atividadeBlog.blog'))

app.register_blueprint(atividadeBlog_blueprint, url_prefix='/atividadeBlog')

if __name__ == '__main__':
    app.run(debug=True)
