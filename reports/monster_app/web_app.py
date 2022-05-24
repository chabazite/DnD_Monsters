from flask import render_template, request, Flask
from flask_bootstrap import Bootstrap
from  flask_wtf import FlaskForm
from sklearn.covariance import graphical_lasso
from wtforms import (validators,SubmitField,SelectField,SelectMultipleField,IntegerField)
import tensorflow as tf
import keras
from keras.models import load_model

app = Flask(__name__)

#Flask-WTF requires encription key
app.config['SECRET_KEY'] = 'NeOoET9Upvp76fobDtppZ8XzIpzEb3sk'

Bootstrap(app)

def load_keras_model():
    """load pretrained keras model """ 
    global model
    model = keras.models.load_model('models\monster_generator.h5')

load_keras_model()


class MonsterForm(FlaskForm):
    """User entry form for entering specifics for monster generation"""
    
    challenge = IntegerField("Enter average level for 4-player party", validators=[validators.InputRequired(), 
                                                                                   validators.NumberRange(min=1,max=20, 
                                                                                                          message='Party level must be between 1 and 20')])
    environment = SelectMultipleField("Enter desired monster environment", validators=[validators.InputRequired()], choices=  ['Arctic', 'Coastal', 'Desert', 'Forest', 'Grassland', 'Hill', 'Mountain', 'NA', 'Swamp', 'Underdark', 'Underwater', 'Urban'])

    monster_type = SelectField("Enter desired monster type", validators=[validators.InputRequired()], choices = ['beast', 'dragon', 'humanoid', 'monstrosity', 'fiend', 'undead', 'elemental',' construct', 'swarm', 'giant', 'plant', 'abberation', 'fey', 'celestial', 'ooze'])
    
    monster_alignment = SelectField("Enter desired monster alignment", validators=[validators.InputRequired()], choices = [ 'any alignment', 'any chaotic alignment', 'any evil alignment', 'any non-good alignment', 'any non-lawful alignment', 'chaotic evil', 'chaotic good', 'chaotic neutral', 'lawful evil', 'lawful good', 'lawful neutral', 'neutral', 'neutral evil', 'neutral good', 'unaligned'])

    difficulty = SelectField("Enter desired difficulty level", default = "medium", validators=[validators.InputRequired()], choices = ['easy', 'medium', 'hard', 'death'])

    submit = SubmitField("Enter")


# define a predict function as an endpoint
@app.route("/", methods=['GET', 'POST'])

def home():
    """Home page of app with form"""
    # Create form
    
    form = MonsterForm(request.form)
    
    # Send template information to index.html

    if request.method == 'POST' and form.validate():
        #extract information
        challenge = int(request.form['challenge'])
        environment = request.form['environment']
        monster_type = request.form['monster_type']
        monster_alignment = request.form ['monster_alignment']
        difficulty = request.form['difficulty']
        return render_template('')

    return render_template('index.html', form=form)



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# keep this as is
if __name__ == '__main__':
    app.run(debug=True)