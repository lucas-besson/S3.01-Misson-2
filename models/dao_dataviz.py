from connexion_db import get_db
from flask import *

from connexion_db import get_db

def dataviz_find_categorie():
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' SELECT cP.nomCategoriePathologie AS LABELLE,COUNT(idPathologie) AS TOTAL
                  FROM Pathologie
                  INNER JOIN categoriePathologie cP on cP.idCategoriePathologie = Pathologie.idCategoriePathologie
                  GROUP BY cP.idCategoriePathologie
                  ORDER BY cP.idCategoriePathologie DESC ;'''
        cursor.execute(sql)
        return cursor.fetchall()
    except ValueError:
        abort(400, 'error requete dataviz_find_categorie')

def dataviz_find_indice():
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' SELECT cP.nomCategoriePathologie AS LABELLE,COUNT(idPathologie) AS TOTAL
                      FROM Pathologie
                      INNER JOIN categoriePathologie cP on cP.idCategoriePathologie = Pathologie.idCategoriePathologie
                      GROUP BY cP.idCategoriePathologie
                      ORDER BY cP.idCategoriePathologie DESC ;'''
        cursor.execute(sql)
        return cursor.fetchall()
    except ValueError:
        abort(400, 'error requete dataviz_find_indice')