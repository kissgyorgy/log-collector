from datetime import datetime
import statistics
from flask import request, jsonify
from . import app, db, filter_by_dim12
from .models import DataPoint


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

    dataset = [d[0] for d in filter_by_dim12(query).all()]

    return jsonify(mean=statistics.mean(dataset))
