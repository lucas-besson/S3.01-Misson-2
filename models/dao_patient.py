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
        sql = ''' DELETE FROM Correspondance WHERE idPatient = %s'''
        cursor.execute(sql, idPatient)
        sql = ''' DELETE FROM estMaladeDe WHERE idPatient = %s'''
        cursor.execute(sql, idPatient)
        sql = ''' DELETE FROM Patient WHERE idPatient = %s'''
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

def patient_add_pathologie(idPatient, idPathologie):
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' INSERT INTO estMaladeDe (idPatient, idPathologie) VALUES (%s, %s)'''
        cursor.execute(sql, (idPatient, idPathologie))
        connection.commit()
        return True
    except ValueError:
        abort(400, 'error requete patient_add_pathologie')

def patient_find_pathologie(idPatient):
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' SELECT estMaladeDe.idPathologie,nomPathologie,estMaladeDe.idPatient
                  FROM estMaladeDe
                  INNER JOIN Pathologie P on estMaladeDe.idPathologie = P.idPathologie 
                  WHERE estMaladeDe.idPatient = %s'''
        cursor.execute(sql, idPatient)
        return cursor.fetchall()
    except ValueError:
        abort(400, 'error requete patient_find_pathologie')

def patient_delete_pathologie(idPatient, idPathologie):
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' DELETE FROM estMaladeDe WHERE idPatient = %s AND idPathologie = %s'''
        cursor.execute(sql, (idPatient, idPathologie))
        connection.commit()
        return True
    except ValueError:
        abort(400, 'error requete patient_delete_pathologie')

def patient_add_medicament(idPatient, idMedicament, idPrescription):
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' INSERT INTO Correspondance (idPatient, idMed,idPrescription) VALUES (%s, %s, %s)'''
        cursor.execute(sql, (idPatient, idMedicament, idPrescription))
        connection.commit()
        return True
    except ValueError:
        abort(400, 'error requete patient_add_medicament')

def patient_find_medicament(idPatient):
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' SELECT Correspondance.idMed,denomination,Correspondance.idPatient,Correspondance.idPrescription
                  FROM Correspondance
                  INNER JOIN Medicament M on Correspondance.idMed = M.idMed 
                  WHERE Correspondance.idPatient = %s'''
        cursor.execute(sql, idPatient)
        return cursor.fetchall()
    except ValueError:
        abort(400, 'error requete patient_add_medicament')

def patient_delete_medicament(idPatient, idMedicament, idPrescription):
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' DELETE FROM Correspondance WHERE idPatient = %s AND idMed = %s AND idPrescription = %s'''
        cursor.execute(sql, (idPatient, idMedicament, idPrescription))
        connection.commit()
        return True
    except ValueError:
        abort(400, 'error requete patient_delete_medicament')

def count_medicament(idPatient):
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' SELECT COUNT(idMed) AS TOTAL
                  FROM Correspondance
                  WHERE idPatient=%s'''
        cursor.execute(sql, idPatient)
        return cursor.fetchone()
    except ValueError:
        abort(400, 'error requete count_medicament')

