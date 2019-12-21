from ch4.app import db, User, Movie

name='Lily'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]
# 添加 add
def add():
    user = User(name=name)
    db.session.add(user)
    for movie in movies:
        m = Movie(title=movie["title"], year=movie["year"])
        db.session.add(m)
    db.session.commit()

# 查询
def query():
    m1 = Movie.query.first()
    print(m1.title,m1.year)
    movies = Movie.query.all()
    for m in movies:
        print(m.title, m.year)
    print(Movie.query.count())
    print(Movie.query.get(1))
    print(r"查询过滤: " + str(Movie.query.filter_by(title='Mahjong').first()))
    print(r"查询过滤(同上):" + str(Movie.query.filter(Movie.title=='Mahjong').first()))

# 更新
def update():
    movie = Movie.query.get(1)
    movie.title='OnePiece'
    movie.year='2006'
    db.session.commit()

# 删除
def delete():
    movie = Movie.query.get(1) # 根据primary_key 查询
    db.session.delete(movie)
    db.session.commit()


if __name__ == '__main__':
    add()
    # query()
    # update()
    # delete()

