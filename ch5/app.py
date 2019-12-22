from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import sys
import os

app = Flask(__name__)
WIN = sys.platform.startswith("win")
if(WIN):
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=prefix+os.path.join(app.root_path , 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)



@app.context_processor
def inject_user():# 函数名可以随意修改
    user = User.query.get(1)
    return dict(user=user)# 需要返回字典，等同于return {'user': user}

@app.route('/')
@app.route('/index')
def index():
    movies = Movie.query.all()
    return render_template('index.html',movies=movies)


@app.errorhandler(404)
def page_not_found(e):

    return render_template('404.html'), 404




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40))
    year = db.Column(db.String(20))