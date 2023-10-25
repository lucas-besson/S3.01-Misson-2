import re
from flask import *

from models.dao_medicament import medicament_find,medicament_find_prescription
from models.dao_patient import *
from models.dao_pathologie import *

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
    find_patho=patient_find_pathologie(idPatient)
    find_medoc=patient_find_medicament(idPatient)
    return render_template('/patient/edit_patient.html', patient=patient, find_patho=find_patho,find_medoc=find_medoc)

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

@patient.route('/patient/add')
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
        message = "Le patient " + nomPatient + " " + prenomPatient + " a bien été ajouté"
        flash(message, 'alert-success')
        return redirect(url_for('patient.show_patient'))

@patient.route('/patient/edit/add_pathologie', methods=['GET'])
def add_patient_pathologie():
    idPatient = request.args.get('idPatient','')
    pathologies = pathologie_find()
    return render_template('/patient/add_patient_pathologie.html', idPatient=idPatient, pathologies=pathologies)


@patient.route('/patient/edit/add_pathologie', methods=['POST'])
def valide_add_patient_pathologie():
    idPatient = request.form.get('idPatient','')
    idPathologie = request.form.get('idPathologie','')
    patient_add_pathologie(idPatient, idPathologie)
    return redirect(url_for('patient.edit_patient', idPatient=idPatient))

@patient.route('/patient/edit/delete_pathologie', methods=['GET'])
def delete_patient_pathologie():
    idPatient = request.args.get('idPatient','')
    idPathologie = request.args.get('idPathologie','')
    patient_delete_pathologie(idPatient, idPathologie)
    return redirect(url_for('patient.edit_patient', idPatient=idPatient))


@patient.route('/patient/edit/add_medicament', methods=['GET'])
def add_patient_medicament():
    idPatient = request.args.get('idPatient','')
    nb_medicament = count_medicament(idPatient)['TOTAL']
    if nb_medicament < 10:
        medicament = medicament_find()
        prescription = medicament_find_prescription()
        return render_template('/patient/add_patient_medicament.html', idPatient=idPatient, medicament=medicament, prescription=prescription)
    else:
        error_message = "Vous avez atteint le nombre maximal de médicaments (10) pour ce patient. Vous pouvez plus en rajouter. Supprmiez en un pour en rajouter un autre"
        flash(error_message, 'alert-danger')
        return redirect(url_for('patient.edit_patient', idPatient=idPatient))

@patient.route('/patient/edit/add_medicament', methods=['POST'])
def valide_add_patient_medicament():
    idPatient = request.form.get('idPatient','')
    idMedicament = request.form.get('idMed','')
    idPrescription = request.form.get('idPrescription', '')
    patient_add_medicament(idPatient, idMedicament, idPrescription)
    return redirect(url_for('patient.edit_patient', idPatient=idPatient))

@patient.route('/patient/edit/delete_medicament', methods=['GET'])
def delete_patient_medicament():
    idPatient = request.args.get('idPatient','')
    idMedicament = request.args.get('idMed','')
    idPrescription = request.args.get('idPrescription', '')
    print("je suis juste ici juste la!!!")
    print(idPrescription)
    patient_delete_medicament(idPatient, idMedicament, idPrescription)
    return redirect(url_for('patient.edit_patient', idPatient=idPatient))



