from connexion_db import get_db
from flask import *

from connexion_db import get_db

def filtrer_patients(filter_word, types, filter_types):
    connection = get_db()
    cursor = connection.cursor()
    sql = '''SELECT Patient.idPatient,nom,prenom,dateNaissance,adresse,codePostale,ville,telephone,GROUP_CONCAT(DISTINCT nomPathologie SEPARATOR ', ') AS nomPathologie, GROUP_CONCAT(DISTINCT nomCategoriePathologie SEPARATOR ', ') AS nomCategoriePathologie,GROUP_CONCAT(DISTINCT codeCIS SEPARATOR ', ') AS CodeCIS
             FROM Patient
             INNER JOIN estMaladeDe emd ON Patient.idPatient = emd.idPatient
             INNER JOIN Pathologie P ON emd.idPathologie = P.idPathologie
             INNER JOIN categoriePathologie cP ON P.idCategoriePathologie = cP.idCategoriePathologie
             INNER JOIN Correspondance C ON Patient.idPatient = C.idPatient
             INNER JOIN Medicament M ON C.idMed = M.idMed'''
    list_param = []
    condition_and = ""

    if filter_word or types or filter_types:
        sql = sql + " WHERE "

    if filter_word:
        sql = sql + " P.nomPathologie LIKE %s "
        recherche = "%" + filter_word + "%"
        list_param.append(recherche)
        condition_and = " AND "

    if types:
        sql = sql + condition_and + "("
        last_item = types[-1]
        for item in types:
            sql = sql + " P.idPathologie = %s "
            if item != last_item:
                sql = sql + " OR "
            list_param.append(item)
        sql = sql + ")"

    if filter_types:
        if filter_word or types:
            condition_and = " AND "
        sql = sql + condition_and + "("
        last_item = filter_types[-1]
        for item in filter_types:
            sql = sql + " cP.idCategoriePathologie = %s "
            if item != last_item:
                sql = sql + " OR "
            list_param.append(item)
        sql = sql + ")"
    sql = sql + " GROUP BY Patient.idPatient, nom, prenom, dateNaissance, adresse, codePostale, ville, telephone"

    tuple_sql = tuple(list_param)
    cursor.execute(sql, tuple_sql)
    return cursor.fetchall()

