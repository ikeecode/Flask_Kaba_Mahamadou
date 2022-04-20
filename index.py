from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, FloatField
from wtforms.validators import InputRequired


#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kaba:ikeecode@localhost/flasko'
# app.config['SECRET_KEY'] = "kfvbsdkfgsfgnkg(_çty( fdbdsd))"
# # initialisation de la base de donnee
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
from models.users import app, db

class AddressForm(FlaskForm):
    street   = StringField('Street', validators=[InputRequired()])
    suite    = StringField('Suite', validators=[InputRequired()])
    city     = StringField('City', validators=[InputRequired()])
    zipcode  = StringField('Zipcode', validators=[InputRequired()])
    lat      = FloatField('Latitude', validators=[InputRequired()])
    lng      = StringField('Longitude', validators=[InputRequired()])
    submit   = SubmitField('Ajouter')



@app.route('/')
def index():
    form = AddressForm()
    return render_template('accueil.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)
