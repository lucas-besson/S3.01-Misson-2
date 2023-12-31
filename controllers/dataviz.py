import re
from flask import *

from models.dao_dataviz import *

from connexion_db import get_db

dataviz = Blueprint('dataviz', __name__, template_folder='templates')

@dataviz.route('/dataviz/show')
def show_dataviz():
    data = dataviz_find_categorie()
    labels_categorie_pathologie = [str(row['LABEL']) for row in data]
    values_categorie_pathologie = [str(row['TOTAL']) for row in data]
    data_indice_pathologie = dataviz_find_indice()
    data_pie = dataviz_pie_indice()
    values_indice = [str(row['STAT']) for row in data_pie]
    labels_indice = [str(row['INDICE']) for row in data_pie]
    return render_template('/dataviz/dataviz.html', labels_categorie_pathologie=labels_categorie_pathologie, values_categorie_pathologie=values_categorie_pathologie, data_indice=data_indice_pathologie, values_indice=values_indice, labels_indice=labels_indice)
