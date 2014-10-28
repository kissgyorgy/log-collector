import click


@click.group()
def logcollector():
    """Run logcollector tasks like create database, start the HTTP server,
    send requests to the server, etc.
    """


@logcollector.command()
def run():
    """Run the development server with debug option."""
    from . import app
    app.debug = True
    app.run(host='0.0.0.0')


@logcollector.command()
@click.option('--drop', is_flag=True, help="Drop tables before create.")
def createdb(drop):
    """Create the database, optionally drop the tables before doing so."""
    from .models import Base
    from . import app, db

    app.config['SQLALCHEMY_ECHO'] = True
    if drop:
        Base.metadata.drop_all(db.engine)
    Base.metadata.create_all(db.engine)


@logcollector.command()
@click.argument('num_data', type=click.INT)
def initdata(num_data):
    """Fill the database with some initial data."""
    from . import db
    from .models import Base, DataPoint

    # Make sure we have the database. Makes no harm if already created.
    Base.metadata.create_all(db.engine)

    datapoints = [
        DataPoint(timestamp=1000000000 + 10 * i,
                  dim1=i, dim2=i % 4, value=10 * i)
        for i in range(1, num_data + 1)
    ]
    db.session.add_all(datapoints)
    db.session.commit()

    num_data = db.session.query(DataPoint).count()
    click.echo('Database filled, has %d datapoints now.' % num_data)


@logcollector.command()
@click.argument('timestamp')
@click.argument('dim1', type=click.INT)
@click.argument('dim2', type=click.INT)
@click.argument('value', type=click.FLOAT)
@click.option('--address', default='http://127.0.0.1:5000',
              help="Where to send the data? 'http://127.0.0.1:5000' by default")
def senddata(timestamp, dim1, dim2, value, address):
    import requests
    from requests import ConnectionError

    try:
        payload = {'timestamp': timestamp, 'dim1': dim1, 'dim2': dim2,
                   'value': value}
        res = requests.post(address + '/new', payload)
    except ConnectionError:
        click.echo("Cannot connect to %s !\nYou can start the server with "
                   "'logcollector run' command!" % address)

    if res.status_code == 201:
        click.echo('Created:')
        click.echo(res.content)


if __name__ == '__main__':
    logcollector()
