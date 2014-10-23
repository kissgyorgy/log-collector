from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError


def floatvalidator(form, field):
    try:
        float(field.data)
    except ValueError:
        raise ValidationError('Float típusú adatnak kell lennie!')


def intvalidator(form, field):
    try:
        int(field.data)
    except ValueError:
        raise ValidationError('Egész számnak kell lennie!')


def timestampvalidator(form, field):
    try:
        datetime.fromtimestamp(float(field.data))
    except ValueError:
        raise ValidationError('Timestampnek kell lennie!')


class NewDataForm(Form):
    timestamp = StringField('Timestamp', validators=[DataRequired(),
                                                     timestampvalidator])
    dim1 = StringField('dim1', validators=[DataRequired(), intvalidator])
    dim2 = StringField('dim2', validators=[DataRequired(), intvalidator])
    value = StringField('value', validators=[DataRequired(), floatvalidator])
