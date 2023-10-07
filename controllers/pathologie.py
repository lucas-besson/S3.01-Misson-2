import re
from flask import *
from models.dao_pathologie import *

from connexion_db import get_db

pathologie = Blueprint('pathologie', __name__, template_folder='templates')

@pathologie.route('/pathologie/show')
def show_pathologie():
    pathologies = find_pathologie()
    return render_template('/pathologie/show_pathologie.html', pathologie=pathologies)