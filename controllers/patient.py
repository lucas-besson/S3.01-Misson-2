import re
from flask import *
from models.dao_patient import *

from connexion_db import get_db

patient = Blueprint('patient', __name__, template_folder='templates')

@patient.route('/patient/show')
def show_patient():
    patients = patient_find()
    return render_template('/patient/show_patient.html', patient=patients)

@patient.route('/patient/delete', methods=['GET'])
def delete_patient():
    idPatient = request.args.get('idPatient')
    patient_delete(idPatient)
    return redirect(url_for('patient.show_patient'))

@patient.route('/patient/edit', methods=['GET'])
def edit_patient():
    idPatient = request.args.get('idPatient')
    patient = patient_find_one(idPatient)
    print(patient)
    return render_template('/patient/edit_patient.html', patient=patient)

@patient.route('/patient/edit', methods=['POST'])
def valide_edit_patient():
    idPatient = request.form.get('idPatient','')
    nomPatient = request.form.get('nomPatient', '')
    prenomPatient = request.form.get('PrenomPatient', '')
    dateNaissancePatient = request.form.get('DateNaissancePatient', '')
    adressePatient = request.form.get('AdressePatient', '')
    villePatient = request.form.get('VillePatient', '')
    codePostalePatient = request.form.get('CodePostalePatient', '')
    telephonePatient = request.form.get('TelPatient', '')
    patient_edit(idPatient, nomPatient, prenomPatient, dateNaissancePatient, adressePatient, villePatient, codePostalePatient, telephonePatient)
    return redirect(url_for('patient.show_patient'))

@patient.route('/patient/add', methods=['GET'])
def add_patient():
    erreurs=[]
    data=[]
    return render_template('/patient/add_patient.html', erreurs=erreurs, data=data)

@patient.route('/patient/add', methods=['POST'])
def valide_add_patient():
    erreurs=[]
    data=[]
    nomPatient = request.form.get('nomPatient', '')
    prenomPatient = request.form.get('PrenomPatient', '')
    dateNaissancePatient = request.form.get('DateNaissancePatient', '')
    adressePatient = request.form.get('AdressePatient', '')
    villePatient = request.form.get('VillePatient', '')
    codePostalePatient = request.form.get('CodePostalePatient', '')
    telephonePatient = request.form.get('TelPatient', '')
    if not nomPatient:
        erreurs.append("Le nom du patient est obligatoire")
    if erreurs:
        return render_template('/patient/add_patient.html', erreurs=erreurs, data=data)
    else:
        patient_add(nomPatient, prenomPatient, dateNaissancePatient, adressePatient, villePatient, codePostalePatient, telephonePatient)
        return redirect(url_for('patient.show_patient'))