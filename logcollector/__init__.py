import functools
from datetime import datetime
from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../logcollector.db'

db = SQLAlchemy(app)


def filter_by_dim12(query):
    for arg in ('dim1', 'dim2'):
        value = request.args.get(arg)
        print(arg, value)
        if value:
            # filtery by dinamic keywords. This way it's possible to extend
            # the function later just by adding a new query argument
            # or even parameterize by which argument to filter the results
            query = query.filter_by(**{arg: value})

    return query


def convert_timestamps(func):
    """Convert first two timestamp arguments to datetime objects."""
    @functools.wraps(func)
    def wrapper(first, second):
        return func(datetime.fromtimestamp(float(first)),
                    datetime.fromtimestamp(float(second))
                    )
    return wrapper


from . import views
