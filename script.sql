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
        libelléStatut VARCHAR(255) NOT NULL,
        PRIMARY KEY(idStatutAdmin)
);

CREATE TABLE ProcedureAutorisation(
        idProcédure INT,
        libelléProcédure VARCHAR(255) NOT NULL,
        PRIMARY KEY(idProcédure)
);

CREATE TABLE Prescription(
        idPrescription INT,
        libelléPrescription VARCHAR(255) NOT NULL,
        PRIMARY KEY(idPrescription)
);

CREATE TABLE Patient(
        idPatient INT,
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
        idPathologie INT,
        nomPathologie VARCHAR(255) NOT NULL,
        PRIMARY KEY(idPathologie)
);

CREATE TABLE Medicament(
        idMed INT,
        codeCIS INT NOT NULL,
        dénomination VARCHAR(255),
        formePharama VARCHAR(255),
        etatCommercialisation BOOLEAN,
        statutBDM VARCHAR(255),
        numUEAutorisation VARCHAR(255),
        titulaire VARCHAR(255),
        surveillance BOOLEAN,
        JJ_MM_AAAA DATE NOT NULL,
        idProcédure INT NOT NULL,
        idStatutAdmin INT NOT NULL,
        PRIMARY KEY(idMed),
        FOREIGN KEY(idProcédure) REFERENCES ProcedureAutorisation(idProcédure),
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


SELECT * FROM VoieAdministration;
SELECT * FROM StatutAdministration;
SELECT * FROM Medicament;
SELECT * FROM Prescription;



SELECT idPathologie,nomPathologie FROM Pathologie


