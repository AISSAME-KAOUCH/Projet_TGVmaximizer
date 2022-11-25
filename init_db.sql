DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

DROP TABLE IF EXISTS profil CASCADE ;
CREATE TABLE profil (
    civilite TEXT, 
    prenom TEXT,  
    nom TEXT, 
    date_de_naissance DATE,
    email TEXT PRIMARY KEY,
    mot_de_passe TEXT
    );

DROP TABLE IF EXISTS trajet CASCADE ;
CREATE TABLE trajet (
    id INT PRIMARY KEY , 
    date DATE, 
    heure_depart TIME, 
    ville_depart TEXT, 
    ville_arrivee TEXT, 
    numero_train INT, 
    heure_arrivee TIME, 
    disponibilite_max TEXT
    );


DROP TABLE IF EXISTS recherche CASCADE ;
CREATE TABLE recherche (
    id INT REFERENCES trajet(id),
    email TEXT REFERENCES profil(email),
    date DATE ,
    heure_depart TIME, 
    ville_depart TEXT,   
    CONSTRAINT pk_recherche PRIMARY KEY(id, email)
    );


