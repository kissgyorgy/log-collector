import statistics
from flask import request, jsonify
from . import app, db, convert_timestamps, query_by_date
from .models import DataPoint
from .moving_average import moving_average


@app.route('/new', methods=['POST'])
def collect():
    new_data = DataPoint(request.form['timestamp'], request.form['dim1'],
                         request.form['dim2'], request.form['value']
                         )
    db.session.add(new_data)
    db.session.commit()

    # return the newly created data, with a 201: CREATED HTTP response
    return jsonify(id=new_data.id, timestamp=request.form['timestamp'],
                   dim1=new_data.dim1, dim2=new_data.dim2,
                   value=new_data.value), 201


@app.route('/mean/<first_timestamp>/<last_timestamp>')
@convert_timestamps
def mean(first_date, last_date):
    dataset = query_by_date(first_date, last_date)
    return jsonify(mean=statistics.mean(dataset))


@app.route('/min/<first_timestamp>/<last_timestamp>')
@convert_timestamps
def min_view(first_date, last_date):
    dataset = query_by_date(first_date, last_date)
    return jsonify(min=min(dataset))


@app.route('/max/<first_timestamp>/<last_timestamp>')
@convert_timestamps
def max_view(first_date, last_date):
    dataset = query_by_date(first_date, last_date)
    return jsonify(max=max(dataset))


@app.route('/stddev/<first_timestamp>/<last_timestamp>')
@convert_timestamps
def stddev(first_date, last_date):
    dataset = query_by_date(first_date, last_date)
    stddev = statistics.stdev(dataset)
    return jsonify(stddev=round(stddev, 5))


@app.route('/movavg/<first_timestamp>/<last_timestamp>/<int:points>')
@convert_timestamps
def movavg(first_date, last_date, points):
    # print(type(first_date), last_date, points)
    dataset = query_by_date(first_date, last_date)
    return jsonify(movavg=moving_average(dataset, points))
