from connexion_db import get_db
from flask import *

def patient_find():
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' SELECT * FROM patient'''
        cursor.execute(sql)
        return cursor.fetchall()
    except ValueError:
        abort(400, 'error requete find_patient')

def patient_delete(idPatient):
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' DELETE FROM Patient WHERE idPatient = %s'''
        print(sql)
        cursor.execute(sql, idPatient)
        connection.commit()
        return True
    except ValueError:
        abort(400, 'error requete delete_patient')

def patient_find_one(idPatient):
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' SELECT * FROM Patient WHERE idPatient = %s'''
        cursor.execute(sql, idPatient)
        return cursor.fetchone()
    except ValueError:
        abort(400, 'error requete patient_find_one')

def patient_edit(idPatient, nomPatient, prenomPatient, dateNaissancePatient, adressePatient, villePatient, codePostalePatient, telephonePatient):
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' UPDATE Patient SET nom = %s, prenom = %s, dateNaissance = %s, adresse = %s, ville = %s, codePostale = %s, telephone = %s
                WHERE idPatient = %s'''
        cursor.execute(sql, (nomPatient, prenomPatient, dateNaissancePatient, adressePatient, villePatient, int(codePostalePatient), telephonePatient, idPatient))
        connection.commit()
        return True
    except ValueError:
        abort(400, 'error requete patient_edit')

def patient_add(nomPatient, prenomPatient, dateNaissancePatient, adressePatient, villePatient, codePostalePatient, telephonePatient):
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' INSERT INTO Patient (nom, prenom, dateNaissance, adresse, codePostale, ville, telephone) VALUES (%s, %s, %s, %s, %s, %s, %s)'''
        cursor.execute(sql, (nomPatient, prenomPatient, dateNaissancePatient, adressePatient, int(codePostalePatient), villePatient, telephonePatient))
        connection.commit()
        return True
    except ValueError:
        abort(400, 'error requete patient_add')