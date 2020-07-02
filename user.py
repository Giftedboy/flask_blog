from flask import Blueprint, render_template, redirect, url_for
from my_diy import my_config
from models import My_blog

user = Blueprint('user',__name__)

@user.route('/')
def index():
    return render_template('user/index.html', **my_config)


@user.route('/articles/')
def articles():
    hasN = 0
    hasB = 0
    try:
        aaa = My_blog.query.order_by(My_blog.creat_time.desc()).paginate(2, per_page=10)
        hasN = 1
    except:
        hasN = 0
    try:
        articles = My_blog.query.order_by(My_blog.creat_time.desc()).paginate(1, per_page=10)
    except:
        articles = ''
    return render_template('user/article.html', **my_config, articles=articles, hasN=hasN, hasB=hasB, page_id = 1)


@user.route('/articles/<int:page_id>/')
def show_page(page_id):
    if page_id == 1:
        return redirect(url_for('user.articles'))
    else:
        hasB = 1
        hasN = 1
        try:
            articles = My_blog.query.order_by(My_blog.creat_time.desc()).paginate(page_id, per_page=10)
        except:
            return redirect(url_for('user.articles'))
        try:
            aaa = My_blog.query.order_by(My_blog.creat_time.desc()).paginate(page_id+1, per_page=10)
        except:
            hasN = 0
        return render_template('user/article.html', **my_config, articles=articles, hasN=hasN, hasB=hasB, page_id=page_id)

        # if articles:
        #     pass
        # else:
        #     return redirect(url_for('user.articles'))


@user.route('/friends/')
def friends():
    return render_template('user/friends.html', **my_config)

