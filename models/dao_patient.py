from connexion_db import get_db
from flask import *

def patient_find():
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' SELECT idPatient FROM Patient'''
        cursor.execute(sql)
        # print(cursor.fetchall())
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
        sql = ''' SELECT idPatient,nomPatient FROM Patient WHERE idPatient = %s'''
        cursor.execute(sql, idPatient)
        return cursor.fetchone()
    except ValueError:
        abort(400, 'error requete patient_find_one')

def patient_edit(idPatient, nomPatient):
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' UPDATE Patient SET nomPatient = %s WHERE idPatient = %s'''
        cursor.execute(sql, (nomPatient, idPatient))
        connection.commit()
        return True
    except ValueError:
        abort(400, 'error requete patient_edit')

def patient_add(nomPatient):
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' INSERT INTO Patient (nomPatient) VALUES (%s)'''
        cursor.execute(sql, nomPatient)
        connection.commit()
        return True
    except ValueError:
        abort(400, 'error requete patient_add')