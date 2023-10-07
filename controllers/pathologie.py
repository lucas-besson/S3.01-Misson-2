import re
from flask import *
from models.dao_pathologie import *

from connexion_db import get_db

pathologie = Blueprint('pathologie', __name__, template_folder='templates')

@pathologie.route('/pathologie/show')
def show_pathologie():
    pathologies = pathologie_find()
    return render_template('/pathologie/show_pathologie.html', pathologie=pathologies)



@pathologie.route('/pathologie/delete', methods=['GET'])
def delete_pathologie():
    idPathologie = request.args.get('idPathologie')
    print("coucou")
    print(idPathologie)
    pathologie_delete(idPathologie)
    return redirect(url_for('pathologie.show_pathologie'))


@pathologie.route('/pathologie/edit', methods=['GET'])
def edit_pathologie():
    idPathologie = request.args.get('idPathologie')
    pathologie = pathologie_find_one(idPathologie)
    return render_template('/pathologie/edit_pathologie.html', pathologie=pathologie)

@pathologie.route('/pathologie/edit', methods=['POST'])
def valide_edit_pathologie():
    idPathologie = request.form.get('idPathologie','')
    nomPathologie = request.form.get('nomPathologie', '')
    pathologie_edit(idPathologie, nomPathologie)
    return redirect(url_for('pathologie.show_pathologie'))

@pathologie.route('/pathologie/add', methods=['GET'])
def add_pathologie():
    erreurs=[]
    data=[]
    return render_template('/pathologie/add_pathologie.html', erreurs=erreurs, data=data)

@pathologie.route('/pathologie/add', methods=['POST'])
def valide_add_pathologie():
    erreurs=[]
    data=[]
    nomPathologie = request.form.get('nomPathologie', '')
    if not nomPathologie:
        erreurs.append("Le nom de la pathologie est obligatoire")
    if erreurs:
        return render_template('/pathologie/add_pathologie.html', erreurs=erreurs, data=data)
    else:
        pathologie_add(nomPathologie)
        return redirect(url_for('pathologie.show_pathologie'))

