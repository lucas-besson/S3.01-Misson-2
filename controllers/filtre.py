import re
from flask import *
from models.dao_pathologie import *
from models.dao_filtre import *
import io
import csv
from flask import Flask, Response
from flask_csv import send_csv

filtre = Blueprint('filtre', __name__, template_folder='templates')

@filtre.route('/visualisation/filtre/show')
def show_filtre():
    filter_word = session.get('filter_word', None)
    types = session.get('types', None)
    filter_types = session.get('filter_types', None)
    items_filtre = filtrer_patients(filter_word, types, filter_types)
    types = pathologie_find()
    filter_types = patholoige_find_categories()
    return render_template('/visualisation/filtre_patient.html', items_filtre=items_filtre, types=types, filter_types=filter_types)

@filtre.route('/visualisation/filtre/download', methods=['POST'])
def export_csv():
    filter_word = session.get('filter_word', None)
    types = session.get('types', None)
    filter_types = session.get('filter_types', None)
    temp = filtrer_patients(filter_word, types, filter_types)
    print("je suis ici")
    print(temp)

    csv_data = "nom;nomPathologie;nomCategoriePathologie\n"
    for i in temp:
        csv_data += i['nom'] + ";" + i['nomPathologie'] + ";"+ i['nomCategoriePathologie'] + "\n"

    with open("patient.csv", "w") as csv_file:
        csv_file.write(csv_data)

    return send_file("patient.csv", as_attachment=True, download_name="patient.csv")

@filtre.route('/visualisation/filtre/send', methods=['POST'])
def filtrer_send():
    filter_word = request.form.get('filter_word', None)
    types = request.form.getlist('types', None)
    filter_types = request.form.getlist('filter_types', None)
    if filter_word or filter_word == "":
        if len(filter_word) > 1:
            if filter_word.isalpha():
                session['filter_word'] = filter_word
            else:
                flash(u'Votre mot recherché doit uniquement être composé de lettres')
        else:
            if len(filter_word) == 1:
                flash(u'Votre mot recherché doit être composé d\'au moins 2 lettres')
            else:
                session.pop('filtrer_word', None)
    if types and types != []:
        if all(number.isdecimal() for number in types):
            session["types"] = types
    if filter_types and filter_types != []:
        if all(number.isdecimal() for number in types):
            session["filter_types"] = filter_types
    return redirect('/visualisation/filtre/show')

@filtre.route('/visualisation/filtre/suppr', methods=['POST'])
def filtrer_suppr():
    session.pop('filter_word', None)
    session.pop('types', None)
    session.pop('filter_types', None)
    return redirect('/visualisation/filtre/show')