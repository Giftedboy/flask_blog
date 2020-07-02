from flask import Flask, render_template, Response, request, jsonify, url_for, redirect, session
from manager import manager
from user import user
import os
import config
from models import db
from exts import db
from models import My_blog
from flask_wtf import CSRFProtect
from my_diy import my_config
from decorater import login_required
from datetime import datetime
"""
from my_diy import my_config
from datetime import datetime
from decorater import login_required, already_login

"""
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['thread'] = 10
app.config.from_object(config)
db.init_app(app)
csrf = CSRFProtect(app)
app.register_blueprint(manager)
app.register_blueprint(user)
"""
@app.route('/')
def index():
    return render_template('index.html', **my_config)


@app.route('/articles/')
def articles():
    return render_template('article.html', my_nickname=my_config['my_nickname'])


@app.route('/friends/')
def friends():
    return render_template('friends.html', my_nickname=my_config['my_nickname'], friends=my_config['friends'])
"""

"""
@app.route('/manager/')
@login_required
def manager():
    return render_template('manager/edit.html', my_nickname=my_config['my_nickname'])




count = 0
time_count = datetime.now()

@app.route('/login/', methods=['GET', 'POST'])
@already_login
def login():
    new_img = '../' + my_config['img_url']
    global count, time_count
    if count >= 3:
        if (datetime.now() - time_count).seconds >= 30:
            count = 0
        return render_template('manager/login.html', **my_config, new_img=new_img, flag=2)
    else:
        if request.method == 'GET':
            return render_template('manager/login.html', **my_config, new_img=new_img)
        else:
                if request.form.get('account') == my_config['account'] and request.form.get('password') == my_config['passwd']:
                    count = 0
                    # 设置 session
                    session['hahaha'] = my_config['passwd']
                    # 登陆成功返回到主页
                    return redirect(url_for('manager'))
                else:
                    count = count + 1
                    if count >= 3:
                        time_count = datetime.now()
                    return render_template('manager/login.html', **my_config, new_img=new_img, flag=1)


@app.route("/manager/create/", methods=["GET", "POST"])
def make_new():
    if request.method == "GET":
        return render_template("manager/NewArt.html", my_nickname=my_config['my_nickname'])

    if request.method == "POST":
        # 获取博客内容
        title = request.form.get("title")
        TextContent = request.form.get("TextContent")
        print(title, TextContent)
        # data = Article(title=title, body=TextContent)
        # db.session.add(data)
        # db.session.commit()
        return render_template("manager/edit.html")
"""


@csrf.error_handler
def handle_csrf_error(e):
    return render_template('errors/csrferror.html', my_nickname=my_config['my_nickname'])

@app.errorhandler(404)
def handle_404_error(err_msg):
    return render_template('errors/404.html', my_nickname=my_config['my_nickname'])

@app.route('/image/<name>')
def image(name):
    with open(os.path.join('.\\static\\upload', name), 'rb') as f:
        resp = Response(f.read(), mimetype="image/jpeg")
    return resp


@csrf.exempt
@app.route('/manager/upload/', methods=['POST'])
@login_required
def upload():
    file = request.files.get('editormd-image-file')
    if not file:
        res = {
            'success': 0,
            'message': '上传失败'
        }
    else:
        ex = os.path.splitext(file.filename)[1]
        filename = datetime.now().strftime('%Y%m%d%H%M%S') + ex
        file.save(".\\static\\upload\\{}".format(filename))
        res = {
            'success': 1,
            'message': '上传成功',
            'url': url_for('image', name=filename)
        }
    return jsonify(res)

@app.route('/p/<int:blog_id>/')
def show_article(blog_id):
    try:
        article = My_blog.query.filter_by(id=blog_id).first()
    except:
        return redirect(url_for('user.index'))
    is_login = 0
    if session.get('hahaha'):
        is_login = 1
        print(is_login)
    print(article.html_body)
    return render_template('user/blog.html', article=article, **my_config, is_login=is_login)


if __name__ == '__main__':
    app.run()
