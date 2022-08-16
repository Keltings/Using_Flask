from flask_wtf import Form
from wtforms import StringField, DateField, IntegerField, \
SelectField, validators
from wtforms.validators import DataRequired

class AddTaskForm(Form):
    task_id = IntegerField()
    dancer_name = StringField('Task Name', validators=[DataRequired()])
    performance_date = DateField(
        'Date Due (mm/dd/yyyy)',
        validators=[DataRequired()], format='%m/%d/%Y'
    )
    genre = SelectField(
        'genre',
        validators=[DataRequired()],
        choices=[
            ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
            ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')
        ]
    )
    status = IntegerField('Status')