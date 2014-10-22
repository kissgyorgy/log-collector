from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../logcollector.db'
db = SQLAlchemy(app)


@app.route("/")
def hello():
    return "Hello World!"
