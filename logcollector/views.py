import statistics
from flask import request, jsonify, render_template
from . import app, db, convert_timestamps, get_dataset_by_dates
from .models import DataPoint
from .moving_average import moving_average
from .forms import NewDataForm


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
@get_dataset_by_dates
def mean(dataset):
    return jsonify(mean=statistics.mean(dataset))


@app.route('/min/<first_timestamp>/<last_timestamp>')
@convert_timestamps
@get_dataset_by_dates
def min_view(dataset):
    return jsonify(min=min(dataset))


@app.route('/max/<first_timestamp>/<last_timestamp>')
@convert_timestamps
@get_dataset_by_dates
def max_view(dataset):
    return jsonify(max=max(dataset))


@app.route('/stddev/<first_timestamp>/<last_timestamp>')
@convert_timestamps
@get_dataset_by_dates
def stddev(dataset):
    stddev = statistics.stdev(dataset)
    return jsonify(stddev=round(stddev, 5))


@app.route('/movavg/<first_timestamp>/<last_timestamp>/<int:points>')
@convert_timestamps
@get_dataset_by_dates
def movavg(dataset, points):
    return jsonify(movavg=moving_average(dataset, points))


@app.route('/new_data', methods=['GET', 'POST'])
def new_data():
    form = NewDataForm()
    if form.validate_on_submit():
        db.session.add(DataPoint(form.timestamp.data,
                                 form.dim1.data,
                                 form.dim2.data,
                                 form.value.data)
        )
        db.session.commit()
    num_data = db.session.query(DataPoint).count()
    new_data = db.session.query(DataPoint).order_by('-id').first()

    return render_template('new_data_form.html', form=form,
                           num_data=num_data, new_data=new_data)
