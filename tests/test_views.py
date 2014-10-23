import json
import pytest
import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from logcollector import app
from logcollector.models import Base, DataPoint


@pytest.fixture
def db():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
    db = SQLAlchemy(app)
    Base.metadata.create_all(db.engine)
    db.session.add_all([
        DataPoint(timestamp='1000000010', dim1=1, dim2=1, value=10),
        DataPoint(timestamp='1000000020', dim1=2, dim2=1, value=20),
        DataPoint(timestamp='1000000030', dim1=3, dim2=2, value=30),
        DataPoint(timestamp='1000000040', dim1=4, dim2=2, value=40),
        DataPoint(timestamp='1000000050', dim1=5, dim2=3, value=50),
    ])
    db.session.commit()

    return db


@pytest.fixture(scope='session')
def test_app():
    return app.test_client()


def to_dict(response):
    return json.loads(response.data.decode())


def test_can_post_new_data(test_app, db):
    assert db.session.query(DataPoint).count() == 5
    test_app.post('/new', data={'timestamp': '1000000060', 'dim1': 6,
                                'dim2': 3, 'value': 60})
    assert db.session.query(DataPoint).count() == 6
    assert db.session.query(DataPoint).get(6).value == 60


def test_mean(test_app, db):
    res = test_app.get('/mean/1000000000/1000000050')
    assert to_dict(res) == {'mean': 25.0}

