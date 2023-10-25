from connexion_db import get_db
from flask import *

from connexion_db import get_db

def dataviz_find_categorie():
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' SELECT cP.nomCategoriePathologie AS LABEL,COUNT(idPathologie) AS TOTAL
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
        sql = '''SELECT P.nom, P.prenom, CEILING(Count( DISTINCT C.idMed)/Count( DISTINCT  M.idPathologie)) AS CALCUL 
                FROM estMaladeDe As M 
                INNER JOIN Correspondance C ON C.idPatient = M.idPatient 
                INNER JOIN Patient P ON M.idPatient = P.idPatient 
                GROUP BY M.idPatient; '''
        cursor.execute(sql)
        return cursor.fetchall()
    except ValueError:
        abort(400, 'error requete dataviz_find_indice')

def dataviz_pie_indice():
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = '''SELECT CALCUL AS INDICE, Count(CALCUL) AS STAT FROM (
                    SELECT CEILING(Count( DISTINCT C.idMed)/Count( DISTINCT  M.idPathologie)) AS CALCUL
                    FROM estMaladeDe As M
                    INNER JOIN Correspondance C ON C.idPatient = M.idPatient
                    INNER JOIN Patient P ON M.idPatient = P.idPatient
                    GROUP BY M.idPatient) As getIndice
                GROUP BY CALCUL;'''
        cursor.execute(sql)
        return cursor.fetchall()
    except ValueError:
        abort(400, 'error requete dataviz_pie_indice')