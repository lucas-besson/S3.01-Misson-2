from connexion_db import get_db
from flask import *


def find_pathologie():
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' SELECT idPathologie,nomPathologie FROM Pathologie'''
        cursor.execute(sql)
        # print(cursor.fetchall())
        return cursor.fetchall()
    except ValueError:
        abort(400, 'error requete find_pathologie')
