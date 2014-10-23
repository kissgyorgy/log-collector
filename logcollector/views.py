import statistics
from flask import request, jsonify
from . import app, db, convert_timestamps, query_by_date
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
@convert_timestamps
def mean(first_date, second_date):
    dataset = query_by_date(first_date, second_date)
    return jsonify(mean=statistics.mean(dataset))


@app.route('/min/<first>/<second>')
@convert_timestamps
def min_view(first_date, second_date):
    dataset = query_by_date(first_date, second_date)
    return jsonify(min=min(dataset))
