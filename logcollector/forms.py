from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class NewDataForm(Form):
    timestamp = StringField('Timestamp', validators=[DataRequired()])
    dim1 = StringField('dim1', validators=[DataRequired()])
    dim2 = StringField('dim2', validators=[DataRequired()])
    value = StringField('value', validators=[DataRequired()])
