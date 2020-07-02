from flask import Blueprint, render_template, request, session, redirect, url_for
from my_diy import my_config
from decorater import login_required, already_login
from datetime import datetime
from models import My_blog
from exts import db

manager = Blueprint('manager', __name__)


@manager.route('/manager/')
@login_required
def index():
    articles = My_blog.query.order_by(My_blog.creat_time.desc()).all()
    return render_template('manager/edit.html', **my_config, articles=articles)


count = 0
time_count = datetime.now()


@manager.route('/login/', methods=['GET', 'POST'])
@already_login
def login():
    global count, time_count
    if count >= 3:
        if (datetime.now() - time_count).seconds >= 30:
            count = 0
        return render_template('manager/login.html', **my_config, flag=2)
    else:
        if request.method == 'GET':
            return render_template('manager/login.html', **my_config)
        else:
                if request.form.get('account') == my_config['account'] and request.form.get('password') == my_config['passwd']:
                    count = 0
                    # 设置 session
                    session['hahaha'] = my_config['passwd']
                    # 登陆成功返回到主页
                    return redirect(url_for('manager.index'))
                else:
                    count = count + 1
                    if count >= 3:
                        time_count = datetime.now()
                    return render_template('manager/login.html', **my_config, flag=1)


@manager.route("/manager/create/", methods=["GET", "POST"])
@login_required
def make_new():
    if request.method == "GET":
        return render_template("manager/NewArt.html", **my_config)

    if request.method == "POST":
        # 获取博客内容
        title = request.form.get("title")
        mkdown_body = request.form.get("TextContent")
        html_body = request.form.get("test-editormd-html-code")
        old_blogid = request.form.get("old_blog")
        if old_blogid != -1:
            try:
                to_del = My_blog.query.filter_by(id=old_blogid).first()
                db.session.delete(to_del)
                db.session.commit()
            except:
                db.session.rollback()
        print(request.form)
        new_art = My_blog(title=title, mkdown_body=mkdown_body, html_body=html_body)
        # data = Article(title=title, body=TextContent)
        try:
            db.session.add(new_art)
            db.session.commit()
        except:
            db.session.rollback()
            # 回到重新编辑页面                          ----------------这里等下要修改
            my_blog = {
                'title': title,
                'mkdown_body':mkdown_body,
            }
            return render_template('manager/NewArt.html', **my_config, my_blog=my_blog)
        return redirect(url_for('manager.index'))


@manager.route('/manager/edit/<int:blog_id>/')
def edit_blog(blog_id):
    try:
        my_blog = My_blog.query.filter_by(id=blog_id).first()
    except:
        redirect(url_for('manager.index'))
    return render_template('manager/NewArt.html', **my_config, my_blog=my_blog)

@manager.route('/manager/delete/<int:blog_id>/')
def delete_blog(blog_id):
    try:
        to_del = My_blog.query.filter_by(id=blog_id).first()
        db.session.delete(to_del)
        db.session.commit()
    except:
        db.session.rollback()
    return redirect(url_for('manager.index'))