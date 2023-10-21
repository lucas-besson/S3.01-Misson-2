from connexion_db import get_db
from flask import *

def medicament_find():
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' SELECT codeCIS,denomination,formePharama,titulaire,surveillance,libelleProcedure AS Proced, libelleStatut AS StatutAdmin
                  FROM Medicament
                  INNER JOIN ProcedureAutorisation PA on Medicament.idProcedure = PA.idProcedure
                  INNER JOIN StatutAdministration SA on Medicament.idStatutAdmin = SA.idStatutAdmin
                  ORDER BY denomination ASC;'''
        cursor.execute(sql)
        return cursor.fetchall()
    except ValueError:
        abort(400, 'error requete find_medicament')

def medicament_delete(idMed):
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' DELETE FROM Medicament WHERE idMed = %s'''
        cursor.execute(sql, idMed)
        connection.commit()
        return True
    except ValueError:
        abort(400, 'error requete delete_medicament')

def medicament_find_one(idMed):
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' SELECT idMed,codeCIS,denomination,formePharama,etatCommercialisation,statutBDM,numUEAutorisation,titulaire,surveillance,JJ_MM_AAAA,libelleProcedure AS Proced, libelleStatut AS StatutAdmin,Medicament.idProcedure,Medicament.idStatutAdmin
                  FROM Medicament
                  INNER JOIN ProcedureAutorisation PA on Medicament.idProcedure = PA.idProcedure
                  INNER JOIN StatutAdministration SA on Medicament.idStatutAdmin = SA.idStatutAdmin
                  WHERE idMed = %s'''
        cursor.execute(sql, idMed)
        return cursor.fetchone()
    except ValueError:
        abort(400, 'error requete medicament_find_one')



def medicament_edit(idMed, codeCIS, denomination, formePharama, etatCommercialisation, statutBDM, numUEAutorisation, titulaire, surveillance, JJ_MM_AAAA, idProcédure, idStatutAdmin):
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' UPDATE Medicament SET codeCIS = %s, denomination = %s, formePharama = %s, etatCommercialisation = %s, statutBDM = %s, numUEAutorisation = %s, titulaire = %s, surveillance = %s, JJ_MM_AAAA = %s, idProcedure = %s, idStatutAdmin = %s WHERE idMed = %s'''
        cursor.execute(sql, (codeCIS, denomination, formePharama, etatCommercialisation, statutBDM, numUEAutorisation, titulaire, surveillance, JJ_MM_AAAA, idProcédure, idStatutAdmin, idMed))
        connection.commit()
        return True
    except ValueError:
        abort(400, 'error requete medicament_edit')

def medicament_add(codeCIS, denomination, formePharama, etatCommercialisation, statutBDM, numUEAutorisation, titulaire, surveillance, JJ_MM_AAAA, idProcédure, idStatutAdmin):
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' INSERT INTO Medicament (codeCIS, denomination, formePharama, etatCommercialisation, statutBDM, numUEAutorisation, titulaire, surveillance, JJ_MM_AAAA, idProcedure, idStatutAdmin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)'''
        cursor.execute(sql, (codeCIS, denomination, formePharama, etatCommercialisation, statutBDM, numUEAutorisation, titulaire, surveillance, JJ_MM_AAAA, idProcédure, idStatutAdmin))
        connection.commit()
        print("ici")
        return True
    except ValueError:
        abort(400, 'error requete medicament_add')

def medicament_find_procdeure():
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' SELECT idProcedure,libelleProcedure FROM ProcedureAutorisation'''
        cursor.execute(sql)
        return cursor.fetchall()
    except ValueError:
        abort(400, 'error requete find_medicament')

def medicament_find_statutAdmin():
    connection = get_db()
    try:
        cursor = connection.cursor()
        sql = ''' SELECT idStatutAdmin,libelleStatut FROM StatutAdministration'''
        cursor.execute(sql)
        return cursor.fetchall()
    except ValueError:
        abort(400, 'error requete find_medicament')