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
    filter_word = session.get('filtrer_word', None)
    types = session.get('types', None)
    items_filtre = filtrer_patients(filter_word, types)
    types = pathologie_find()
    return render_template('/visualisation/filtre_patient.html', items_filtre=items_filtre, types=types)

@filtre.route('/visualisation/filtre/download', methods=['POST'])
def export_csv():
    filter_word = session.get('filtrer_word', None)
    types = session.get('types', None)
    temp = filtrer_patients(filter_word, types)

    csv_data = "nom;nomPathologie\n"
    for i in temp:
        csv_data += i['nom'] + ";" + i['nomPathologie'] + "\n"

    with open("patient.csv", "w") as csv_file:
        csv_file.write(csv_data)

    return send_file("patient.csv", as_attachment=True, download_name="patient.csv")

@filtre.route('/visualisation/filtre/send', methods=['POST'])
def filtrer_send():
    filter_word = request.form.get('filter_word', None)
    types = request.form.getlist('types', None)
    if filter_word or filter_word == "":
        if len(filter_word) > 1:
            if filter_word.isalpha():
                session['filtrer_word'] = filter_word
            else:
                flash(u'Votre mot recherché doit uniquement être composé de lettres')
        else:
            if len(filter_word) == 1:
                flash(u'Votre mot recherché doit être composé d\'au moins 2 lettres')
            else:
                session.pop('filtrer_word', None)
    if types and types != []:
        #print(f"types: {types}")
        if all(number.isdecimal() for number in types):
            session["types"] = types
    return redirect('/visualisation/filtre/show')

@filtre.route('/visualisation/filtre/suppr', methods=['POST'])
def filtrer_suppr():
    session.pop('filtrer_word', None)
    session.pop('types', None)
    return redirect('/visualisation/filtre/show')