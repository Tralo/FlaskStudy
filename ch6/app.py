from flask import url_for, request, Flask,redirect, flash,render_template
import os,sys

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
WIN = sys.platform.startswith("win")
if(WIN):
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=prefix+os.path.join(app.root_path , 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = 'dev'  # 等同于 app.secret_key = 'dev'
db = SQLAlchemy(app)

from ch6.Model import User, Movie

@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'),404

@app.context_processor
def inject_user():
    user = User.query.get(1)
    return dict(user=user)

@app.route('/', methods=['GET', 'POST'])  # 注意GET POST 是大写
def index():
    if request.method == 'POST':
        # 获取表单数据
        title = request.form.get('title')
        year = request.form.get('year')
        # 验证数据
        if not title or not year or len(year) > 4 or len(title) > 60:
            flash('Invalid input.')  # 显示错误提示
            return redirect(url_for('index'))  # 重定向回主页
        # 保存表单数据到数据库
        movie = Movie(title=title, year=year)
        print(title, year)
        db.session.add(movie)
        db.session.commit()
        flash('Item created.')
        return redirect(url_for('index'))
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)



@app.route('/movie/edit/<int:movie_id>',methods=['GET', 'POST'])
def edit(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    if request.method == 'POST':
        id = request.form.get('id')
        title = request.form.get('title')
        year = request.form.get('year')
        # 验证数据
        if not title or not year or len(year) > 4 or len(title) > 60:
            flash('Invalid update.')  # 显示错误提示
            return redirect(url_for('edit', movie_id=movie_id))  # 重定向回主页
        # 保存表单数据到数据库
        movie.title = title
        movie.year = year
        db.session.commit()
        flash('Item Edited.')
        return redirect(url_for('index'))
    return render_template('edit.html', movie=movie)


@app.route('/movie/delete/<int:movie_id>', methods=['GET'])
def delete(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash('Item Deleted.')
    return redirect(url_for('index'))