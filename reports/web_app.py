from wtforms import (Form,validators,SubmitField,SelectField,IntegerField)
from flask import render_template
import flask
from flask import request
class ReusableForm(Form):
    """User entry form for entering specifics for generation"""
    
    # challange input
    challange = IntegerField("Enter average level for 4-player party", validators=[validators.InputRequired(), 
                                                                                   validators.NumberRange(min=1,max=20, 
                                                                                                          message='Party level must be between 1 and 20')])
    # Environment Input
    environment = SelectField("Enter desired monster environment", validators=[validators.InputRequired()])

    monster_type = SelectField("Enter desired monster type", validators=[validators.InputRequired()])

    difficulty = SelectField("Enter desired difficulty level", default = "medium", validators=[validators.InputRequired()])

    submit = SubmitField("Enter")

app = flask.Flask(__name__)

# define a predict function as an endpoint
@app.route("/", methods=['GET', 'POST'])
def home():
    """Home page of app with form"""
    # Create form
    form = ReusableForm(request.form)

    # Send template information to index.html
    return render_template('index.html', form=form)
app.run(host='0.0.0.0')