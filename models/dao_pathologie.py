from connexion_db import get_db
from flask import *


def pathologie_find():
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' SELECT idPathologie,nomPathologie, C.nomCategoriePathologie FROM Pathologie As P INNER JOIN categoriePathologie As C ON P.idCategoriePathologie = C.idCategoriePathologie ORDER BY 1'''
        cursor.execute(sql)
        return cursor.fetchall()
    except ValueError:
        abort(400, 'error requete find_pathologie')


def pathologie_delete(idPathologie):
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' DELETE FROM estMaladeDe WHERE idPathologie = %s'''
        cursor.execute(sql, idPathologie)
        sql = ''' DELETE FROM Pathologie WHERE idPathologie = %s'''
        cursor.execute(sql, idPathologie)
        connection.commit()
        return True
    except ValueError:
        abort(400, 'error requete delete_pathologie')

def pathologie_find_one(idPathologie):
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' SELECT idPathologie,nomPathologie,idCategoriePathologie FROM Pathologie WHERE idPathologie = %s'''
        cursor.execute(sql, idPathologie)
        return cursor.fetchone()
    except ValueError:
        abort(400, 'error requete pathologie_find_one')

def pathologie_edit(idPathologie, nomPathologie, categoriePathologie):
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' UPDATE Pathologie SET nomPathologie = %s,idCategoriePathologie=%s  WHERE idPathologie = %s'''
        cursor.execute(sql, (nomPathologie,categoriePathologie, idPathologie))
        connection.commit()
        return True
    except ValueError:
        abort(400, 'error requete pathologie_edit')

def pathologie_add(nomPathologie,categoriePathologie):
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' INSERT INTO Pathologie (nomPathologie,idCategoriePathologie) VALUES (%s,%s)'''
        cursor.execute(sql, (nomPathologie,categoriePathologie))
        connection.commit()
        return True
    except ValueError:
        abort(400, 'error requete pathologie_add')


def patholoige_find_categories():
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' SELECT idCategoriePathologie,nomCategoriePathologie FROM categoriePathologie ORDER BY idCategoriePathologie DESC '''
        cursor.execute(sql)
        return cursor.fetchall()
    except ValueError:
        abort(400, 'error requete pathologie_find_categories')
