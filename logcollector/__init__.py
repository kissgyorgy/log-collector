from datetime import datetime
import statistics
from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from .models import DataPoint


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../logcollector.db'
db = SQLAlchemy(app)


@app.route('/new', methods=['POST'])
def collect():
    new_data = DataPoint(request.form['timestamp'], request.form['dim1'],
                         request.form['dim2'], request.form['value']
                         )
    db.session.add(new_data)
    db.session.commit()

    return jsonify(id=new_data.id, timestamp=request.form['timestamp'],
                   dim1=new_data.dim1, dim2=new_data.dim2), 201


@app.route('/mean/<first>/<second>')
def mean(first, second):
    first_date = datetime.fromtimestamp(float(first))
    second_date = datetime.fromtimestamp(float(second))

    query = db.session.query(DataPoint.value)\
                      .filter(first_date <= DataPoint.timestamp,
                              DataPoint.timestamp <= second_date)

    dim1 = request.args.get('dim1')
    if dim1:
        query = query.filter_by(dim1=dim1)

    dim2 = request.args.get('dim2')
    if dim2:
        query = query.filter_by(dim2=dim2)

    dataset = [d[0] for d in query.all()]

    return jsonify(mean=statistics.mean(dataset))
