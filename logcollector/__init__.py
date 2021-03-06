import functools
from datetime import datetime
from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy
from .models import DataPoint


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../logcollector.db'
app.config['SECRET_KEY'] = "k_Ex`3\x06谍~\x11G扃Tmҡ9n&`'c5"

db = SQLAlchemy(app)


def filter_by_dim12(query):
    """Filter query by values of dim1 and dim2 arguments."""
    for arg in ('dim1', 'dim2'):
        value = request.args.get(arg)
        if value:
            # filtery by dinamic keywords. This way it's possible to extend
            # the function later just by adding a new query argument
            # or even parameterize by which argument to filter the results
            query = query.filter_by(**{arg: value})

    return query


def convert_timestamps(func):
    """Convert first two timestamp arguments to datetime objects."""
    @functools.wraps(func)
    def wrapper(first_timestamp, last_timestamp, *args, **kwargs):
        return func(datetime.fromtimestamp(float(first_timestamp)),
                    datetime.fromtimestamp(float(last_timestamp)),
                    *args, **kwargs
                    )
    return wrapper


def get_dataset_by_dates(view):
    """Query the database for a dataset in a given time frame."""
    @functools.wraps(view)
    def wrapper(first_date, last_date, points=None):
        query = db.session.query(DataPoint.value)\
                          .filter(first_date <= DataPoint.timestamp,
                                  DataPoint.timestamp <= last_date)

        dataset = [d[0] for d in filter_by_dim12(query).all()]

        if points:
            return view(dataset, points)
        else:
            return view(dataset)

    return wrapper


from . import views
