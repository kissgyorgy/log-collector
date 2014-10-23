import json
from logcollector.models import DataPoint


def to_dict(response):
    return json.loads(response.data.decode())


def test_can_post_new_data(test_app, db):
    assert db.session.query(DataPoint).count() == 5
    test_app.post('/new', data={'timestamp': '1000000060', 'dim1': 6,
                                'dim2': 3, 'value': 60})
    assert db.session.query(DataPoint).count() == 6
    assert db.session.query(DataPoint).get(6).value == 60


class TestMean:
    def test_mean(self, test_app, db):
        res = test_app.get('/mean/1000000000/1000000050')
        assert to_dict(res) == {'mean': 30.0}

    def test_mean_with_dim1(self, test_app):
        res = test_app.get('/mean/1000000000/1000000050?dim1=1')
        assert to_dict(res) == {'mean': 10}

    def test_mean_with_dim2(self, test_app):
        res = test_app.get('/mean/1000000000/1000000050?dim2=1')
        assert to_dict(res) == {'mean': 15}

    def test_mean_with_dim1_and_dim2(self, test_app, db):
        db.session.add(DataPoint('1000000060', 5, 3, 60))
        db.session.commit()
        res = test_app.get('/mean/1000000000/1000000060?dim1=5&dim2=3')
        assert to_dict(res) == {'mean': 55.0}


class TestMin:
    def test_min(self, test_app):
        res = test_app.get('/min/1000000000/1000000050')
        assert to_dict(res) == {'min': 10}

    def test_min_with_dim1(self, test_app):
        res = test_app.get('/min/1000000000/1000000050?dim1=2')
        assert to_dict(res) == {'min': 20}

    def test_min_with_dim2(self, test_app):
        res = test_app.get('/min/1000000000/1000000050?dim2=2')
        assert to_dict(res) == {'min': 30}

    def test_min_with_dim1_and_dim2(self, test_app, db):
        db.session.add(DataPoint('1000000060', 5, 3, 60))
        db.session.commit()
        res = test_app.get('/min/1000000000/1000000060?dim1=5&dim2=3')
        assert to_dict(res) == {'min': 50}

