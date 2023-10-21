import re
from flask import *

from models.dao_dataviz import *

from connexion_db import get_db

dataviz = Blueprint('dataviz', __name__, template_folder='templates')

@dataviz.route('/dataviz/show')
def show_dataviz():
    data = dataviz_find()
    labels_categorie_pathologie = [str(row['LABELLE']) for row in data]
    values_categorie_pathologie = [str(row['TOTAL']) for row in data]
    return render_template('/dataviz/dataviz.html', labels_categorie_pathologie=labels_categorie_pathologie, values_categorie_pathologie=values_categorie_pathologie)