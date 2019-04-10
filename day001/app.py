# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/10 17:22
# 文件名称: 数据库测试.py
# 开发工具: PyCharm
# 导入:
from flask import Flask
from flask import render_template as render
import os
# 读取Excel的依赖
import pandas as pd
# 创建数据库的依赖
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)


@app.route('/')
def index():
    return render('index.html')


# 读取Excel表的方法
@app.route('/read_excel')
def read_excel():
    # 读取 调用pandas自带功能可以一键读取
    data = pd.read_excel('Ejemplo MerchantSettlement-20190408-20190411.xlsx')
    print(data)
    return render("index.html")


if __name__ == '__main__':
    db.create_all()
    app.run()
