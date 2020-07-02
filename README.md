# flask_blog

## 样例

http://106.54.55.28:5000/


## 注意点
flask学习过程中做的个人博客，功能比较少，管理后台只有写文章的功能，其他配置全在 my_div.py 统一设置

其中在 static/editormd文件夹内容全为开源项目 [editor.md](https://github.com/pandao/editor.md ) 里的内容，下载下来复制进去即可

关于 `my_diy.py`:
```
my_config = {
    'my_nickname': 'R0oKi3',  # 昵称
    'img_name': "index.png",  # 头像, 将自己的头像放在 static/images 文件夹下即可，然后修改此处的值为文件名即可
    'ico_name': 'favicon.ico',  # 网页标签栏的 ico ，操作同上
    'my_moto': '人生若只如初见，何事秋风悲画扇。',  # 首页动态打印的字符
    'about_me': {'QQ': '2309896932', 'WeChat': 'douwannadancetoo', },  # 个人信息,可以继续添加
    'account': 'root',  # 设置账号
    'passwd': 'root',  # 设置密码
    'friends': {'天下大木头': 'https://www.wjlshare.xyz', 'Dy_c': 'https://npc.witctf.cn', },  # 友情链接,可以继续添加
}
```

## 如何快速搭建测试
* 下载 phpstudy ，启动 mysql 环境

* 修改 config.py 配置文件
```
HOSTNAME = '127.0.0.1'  # 数据库的地址
PORT = '3306'  # 端口
DATABASE = 'my_blog'  # 数据库名
USERNAME = 'myblog'  # 数据库账号
PASSWORD = 'qwe123'  # 数据库密码
```

* 在 phpstudy 里创建一个 数据库，为自己在 congfig.py 中定义好的

* pip install -r requirements.txt

* python3 manage.py db init

* python3 manage.py db migrate

* python3 manage.py db upgrade

* python3 -m flask run

## 关于后台
在首页连点 **3** 下头像即可进入后台

## 关于 blog 样式

借鉴了 [cnblogs-theme-silence](https://github.com/esofar/cnblogs-theme-silence)，以及 [大师傅key](https://gh0st.cn/) 的一些元素


## 关于安全性
没有安全性可言，自己已知的就有一个管理后台越权
只能说自己太菜了

