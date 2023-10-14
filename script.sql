DROP TABLE IF EXISTS est_malade_de;
DROP TABLE IF EXISTS Correspondance;
DROP TABLE IF EXISTS Medicament;
DROP TABLE IF EXISTS Pathologie;
DROP TABLE IF EXISTS Patient;
DROP TABLE IF EXISTS Prescription;
DROP TABLE IF EXISTS ProcedureAutorisation;
DROP TABLE IF EXISTS StatutAdministration;

CREATE TABLE StatutAdministration(
        idStatutAdmin INT,
        libelleStatut VARCHAR(255) NOT NULL,
        PRIMARY KEY(idStatutAdmin)
);

CREATE TABLE ProcedureAutorisation(
        idProcedure INT,
        libelleProcedure VARCHAR(255) NOT NULL,
        PRIMARY KEY(idProcedure)
);

CREATE TABLE Prescription(
        idPrescription INT,
        libelléPrescription VARCHAR(255) NOT NULL,
        PRIMARY KEY(idPrescription)
);

CREATE TABLE Patient(
        idPatient INT AUTO_INCREMENT,
        nom VARCHAR(255),
        prenom VARCHAR(255),
        dateNaissance DATE NOT NULL,
        adresse VARCHAR(255),
        codePostale INT NOT NULL,
        ville VARCHAR(255),
        telephone BIGINT NOT NULL,
        PRIMARY KEY(idPatient)
);

CREATE TABLE Pathologie(
        idPathologie INT AUTO_INCREMENT,
        nomPathologie VARCHAR(255) NOT NULL,
        PRIMARY KEY(idPathologie)
);

CREATE TABLE Medicament(
        idMed INT AUTO_INCREMENT,
        codeCIS INT NOT NULL,
        denomination VARCHAR(255),
        formePharama VARCHAR(255),
        etatCommercialisation VARCHAR(255),
        statutBDM VARCHAR(255),
        numUEAutorisation VARCHAR(255),
        titulaire VARCHAR(255),
        surveillance VARCHAR(255),
        JJ_MM_AAAA DATE NOT NULL,
        idProcedure INT NOT NULL,
        idStatutAdmin INT NOT NULL,
        PRIMARY KEY(idMed),
        FOREIGN KEY(idProcedure) REFERENCES ProcedureAutorisation(idProcedure),
        FOREIGN KEY(idStatutAdmin) REFERENCES StatutAdministration(idStatutAdmin)
);


CREATE TABLE Correspondance(
        idMed INT,
        idPrescription INT,
        idPatient INT,
        PRIMARY KEY(idMed, idPrescription, idPatient),
        FOREIGN KEY(idMed) REFERENCES Medicament(idMed),
        FOREIGN KEY(idPrescription) REFERENCES Prescription(idPrescription),
        FOREIGN KEY(idPatient) REFERENCES Patient(idPatient)
);

CREATE TABLE est_malade_de(
        idPatient INT,
        idPathologie INT,
        PRIMARY KEY(idPatient, idPathologie),
        FOREIGN KEY(idPatient) REFERENCES Patient(idPatient),
        FOREIGN KEY(idPathologie) REFERENCES pathologie(idPathologie)
);

LOAD DATA LOCAL INFILE '/Users/lucasbesson/Desktop/IUT_RDS/SAE/S3.01-Misson-2/DataDB/statut_administration.csv' INTO TABLE StatutAdministration FIELDS TERMINATED BY ';';
LOAD DATA LOCAL INFILE '/Users/lucasbesson/Desktop/IUT_RDS/SAE/S3.01-Misson-2/DataDB/procedure_autorisation.csv' INTO TABLE ProcedureAutorisation FIELDS TERMINATED BY ';';
LOAD DATA LOCAL INFILE '/Users/lucasbesson/Desktop/IUT_RDS/SAE/S3.01-Misson-2/DataDB/prescription.csv' INTO TABLE Prescription FIELDS TERMINATED BY ';';
LOAD DATA LOCAL INFILE '/Users/lucasbesson/Desktop/IUT_RDS/SAE/S3.01-Misson-2/DataDB/pathologie.csv' INTO TABLE Pathologie FIELDS TERMINATED BY ';';
LOAD DATA LOCAL INFILE '/Users/lucasbesson/Desktop/IUT_RDS/SAE/S3.01-Misson-2/DataDB/medicament.csv' INTO TABLE Medicament FIELDS TERMINATED BY ';';


SELECT * FROM StatutAdministration;
SELECT * FROM Medicament;
SELECT * FROM Prescription;


INSERT INTO Patient (nom, prenom, dateNaissance, adresse, codePostale, ville, telephone)
VALUES ('lucas', 'besson', '2003-09-26', 'TEST ADRESSE', 75000, 'PARIS', 0677777777);

INSERT INTO Patient (nom, prenom, dateNaissance, adresse, codePostale, ville, telephone)
VALUES ('leo', 'corutois', '2003-09-16', 'TEST ADRESSE', 75000, 'PARIS', 0677777777);

SELECT * FROM Patient;

INSERT INTO est_malade_de(idPatient,idPathologie) VALUES (1,1);
INSERT INTO est_malade_de(idPatient,idPathologie) VALUES (2,2);

SELECT * FROM est_malade_de;

SELECT nom,nomPathologie
FROM Patient
INNER JOIN est_malade_de emd on Patient.idPatient = emd.idPatient
INNER JOIN Pathologie P on emd.idPathologie = P.idPathologie
WHERE P.idPathologie=2;



SELECT idPathologie,nomPathologie
FROM Pathologie
ORDER BY nomPathologie;



SELECT idProcedure,libelleProcedure FROM ProcedureAutorisation
