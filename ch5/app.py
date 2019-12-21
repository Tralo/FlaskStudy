from flask import Flask,render_template


def page_not_found(e):

    user = User.query.first()
    return render_template('404.html', user=user), 404




