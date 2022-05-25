from flask import render_template, request, Flask
from flask_bootstrap import Bootstrap
from  flask_wtf import FlaskForm
from sklearn.covariance import graphical_lasso
from wtforms import (validators,SubmitField,SelectField,SelectMultipleField,IntegerField)
import tensorflow as tf
import keras
from keras.models import load_model
import numpy as np
import plotly
import plotly.express as px
import json

app = Flask(__name__)

#Flask-WTF requires encription key
app.config['SECRET_KEY'] = 'NeOoET9Upvp76fobDtppZ8XzIpzEb3sk'

Bootstrap(app)

def load_keras_model():
    """load pretrained keras model """ 
    global model
    model = keras.models.load_model('models\monster_generator.h5')

load_keras_model()

environ = [0,0,0,0,0,0,0,0,0,0,0,0]
type =  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
alignment = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

class MonsterForm(FlaskForm):
    """User entry form for entering specifics for monster generation"""
    
    challenge = IntegerField("Enter average level for 4-player party", validators=[validators.InputRequired(), 
                                                                                   validators.NumberRange(min=1,max=20, 
                                                                                                          message='Party level must be between 1 and 20')])
    size = SelectField("Enter desired monster size", validators=[validators.InputRequired()], choices=  [(1,'Tiny'), (2,'Small'), (3,'Medium'), (4,'Large'), (5,'Huge'), (6,'Gargantuan')])
    environment = SelectField("Enter desired monster environment", validators=[validators.InputRequired()], choices=  [(0,'Arctic'), (1,'Coastal'), (2,'Desert'), (3,'Forest'), (4,'Grassland'), (5,'Hill'), (6,'Mountain'), (7,'NA'), (8,'Swamp'), (9,'Underdark'), (10,'Underwater'), (11,'Urban')])

    monster_type = SelectField("Enter desired monster type", validators=[validators.InputRequired()], choices = [(0,'beast'), (1,'dragon'), (2,'humanoid'), (3,'monstrosity'), (4,'fiend'), (5,'undead'), (6,'elemental'),(7,'construct'), (8,'swarm'), (9,'giant'), (10,'plant'), (11,'abberation'), (12,'fey'), (13,'celestial'), (14,'ooze')])
    
    monster_alignment = SelectField("Enter desired monster alignment", validators=[validators.InputRequired()], choices = [(0,'any alignment'), (1,'any chaotic alignment'), (2,'any evil alignment'), (3,'any non-good alignment'), (4,'any non-lawful alignment'), (5,'chaotic evil'), (6,'chaotic good'), (7,'chaotic neutral'), (8,'lawful evil'), (9,'lawful good'), (10,'lawful neutral'), (11,'neutral'), (12,'neutral evil'), (13,'neutral good'), (14,'unaligned')])

    difficulty = SelectField("Enter desired difficulty level", default = "medium", validators=[validators.InputRequired()], choices = [(-5,'easy'), (0,'medium'), (5,'hard'), (10,'deadly')])

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
        environment = int(request.form['environment'])
        monster_type = int(request.form['monster_type'])
        monster_alignment = int(request.form ['monster_alignment'])
        difficulty = int(request.form['difficulty'])
        size = int(request.form['size'])

        #create numpy array for prediction
        environ[environment] = 1
        type[monster_type] =1
        alignment[monster_alignment] = 1
        challenge_r = [challenge + difficulty]
        size_r= [size]


        final_array = np.concatenate((challenge_r,size_r,environ,type,alignment))
        
        pred = model.predict(final_array)
        return pred


    return render_template('index.html', form=form)

@app.route('/monster')
def monster_stats():
    df = pd.DataFrame(data = pred.astype(int), columns=['Hit Points','Armor Class','Proficiency Bonus','STR','DEX','CON','WIS','INT','CHA', 'STR_SV','DEX_SV','CON_SV','WIS_SV','INT_SV','CHA_SV', 'Attack_Bonus','Average_Damage_per_Round','Legendary Actions', 'Damage Resistances', 'Damage Immunities', 'Condition Immunities', 'Damage Vulnerabilities', 'Legendary Resistance', 'Magic Resistance'])

    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    fig.update_traces(fill='toself')
    fig.show()

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('monster_stats.html', graphJSON=graphJSON)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# keep this as is
if __name__ == '__main__':
    app.run(debug=True)