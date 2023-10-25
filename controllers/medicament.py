import re
from flask import *
from models.dao_medicament import *

medicament = Blueprint('medicament', __name__, template_folder='templates')

@medicament.route('/medicament/show')
def show_medicament():
    medicaments = medicament_find()
    return render_template('/medicament/show_medicament.html', medicament=medicaments)

@medicament.route('/medicament/delete', methods=['GET'])
def delete_medicament():
    idMed = request.args.get('idMed')
    medicament_delete(idMed)
    return redirect(url_for('medicament.show_medicament'))

@medicament.route('/medicament/edit', methods=['GET'])
def edit_medicament():
    idMed = request.args.get('idMed')
    medicament = medicament_find_one(idMed)
    procedure = medicament_find_procdeure()
    statutAdmin = medicament_find_statutAdmin()
    return render_template('/medicament/edit_medicament.html', medicament=medicament, procedure=procedure, statutAdmin=statutAdmin)

@medicament.route('/medicament/edit', methods=['POST'])
def valide_edit_medicament():
    idMed = request.form.get('idMed','')
    codeCIS = request.form.get('codeCIS', '')
    denomination = request.form.get('denomination', '')
    formePharama = request.form.get('formePharama', '')
    etatCommercialisation = request.form.get('etatCommercialisation', '')
    statutBDM = request.form.get('statutBDM', '')
    numUEAutorisation = request.form.get('numUEAutorisation', '')
    titulaire = request.form.get('titulaire', '')
    surveillance = request.form.get('surveillance', '')
    JJ_MM_AAAA = request.form.get('JJ_MM_AAAA', '')
    idProcédure = request.form.get('idProcedure', '')
    idStatutAdmin = request.form.get('idStatutAdmin', '')
    medicament_edit(idMed, codeCIS, denomination, formePharama, etatCommercialisation, statutBDM, numUEAutorisation, titulaire, surveillance, JJ_MM_AAAA, idProcédure, idStatutAdmin)
    return redirect(url_for('medicament.show_medicament'))

@medicament.route('/medicament/add')
def add_medicament():
    erreurs=[]
    data=[]
    procedure = medicament_find_procdeure()
    statutAdmin = medicament_find_statutAdmin()
    return render_template('/medicament/add_medicament.html', erreurs=erreurs, data=data, procedure=procedure, statutAdmin=statutAdmin)

@medicament.route('/medicament/add', methods=['POST'])
def valide_add_medicament():
    erreurs = []
    data = []
    codeCIS = request.form.get('codeCIS', '')
    denomination = request.form.get('denomination', '')
    formePharama = request.form.get('formePharama', '')
    etatCommercialisation = request.form.get('etatCommercialisation', '')
    statutBDM = request.form.get('statutBDM', '')
    numUEAutorisation = request.form.get('numUEAutorisation', '')
    titulaire = request.form.get('titulaire', '')
    surveillance = request.form.get('surveillance', '')
    JJ_MM_AAAA = request.form.get('JJ_MM_AAAA', '')
    idProcédure = request.form.get('idProcedure', '')
    idStatutAdmin = request.form.get('idStatutAdmin', '')
    if not codeCIS:
        erreurs.append("Le code CIS est obligatoire")
    if not denomination:
        erreurs.append("La dénomination est obligatoire")
    if not formePharama:
        erreurs.append("La forme pharmaceutique est obligatoire")
    if not statutBDM:
        erreurs.append("Le statut BDM est obligatoire")
    if not numUEAutorisation:
        erreurs.append("Le numéro d'UE d'autorisation est obligatoire")
    if not titulaire:
        erreurs.append("Le titulaire est obligatoire")
    if not JJ_MM_AAAA:
        erreurs.append("La date d'autorisation est obligatoire")
    if not idProcédure:
        erreurs.append("La procédure est obligatoire")
    if not idStatutAdmin:
        erreurs.append("Le statut administratif est obligatoire")
    if erreurs:
        return render_template('/medicament/add_medicament.html', erreurs=erreurs, data=data)
    else:
        medicament_add(codeCIS, denomination, formePharama, etatCommercialisation, statutBDM, numUEAutorisation, titulaire, surveillance, JJ_MM_AAAA, idProcédure, idStatutAdmin)
        return redirect(url_for('medicament.show_medicament'))

