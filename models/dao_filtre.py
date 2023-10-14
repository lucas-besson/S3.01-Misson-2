from connexion_db import get_db
from flask import *

from connexion_db import get_db

def filtrer_patients(filter_word, types):
    connection = get_db()
    cursor = connection.cursor()
    sql = '''SELECT nom, nomPathologie
             FROM Patient
             INNER JOIN est_malade_de emd on Patient.idPatient = emd.idPatient
             INNER JOIN Pathologie P on emd.idPathologie = P.idPathologie'''
    list_param = []
    condition_and = ""

    if filter_word or types:
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

    tuple_sql = tuple(list_param)
    cursor.execute(sql, tuple_sql)
    return cursor.fetchall()

