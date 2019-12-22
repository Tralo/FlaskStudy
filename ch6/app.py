from flask import url_for, request, Flask,redirect
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
db = SQLAlchemy(app)
