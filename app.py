from flask import Flask, request, render_template, redirect, flash, session, g
from flask import Blueprint

from controllers import pathologie
from controllers import patient
from controllers import filtre
from controllers import medicament
from controllers.pathologie import *
from controllers.patient import *
from controllers.filtre import *
from controllers.medicament import *
from controllers.dataviz import *

app = Flask(__name__)
app.secret_key = 'une cle(token) : grain de sel(any random string)'

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
@app.route('/')
def show_accueil():
    return render_template('layout.html')

app.register_blueprint(pathologie)
app.register_blueprint(patient)
app.register_blueprint(filtre)
app.register_blueprint(medicament)
app.register_blueprint(dataviz)

if __name__ == '__main__':
    app.run()


