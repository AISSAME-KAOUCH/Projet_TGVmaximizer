DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

CREATE TABLE profil (
    civilite TEXT, 
    prenom TEXT,  
    nom TEXT, 
    date_de_naissance DATE,
    email TEXT PRIMARY KEY,
    mot_de_passe TEXT
    );

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


CREATE TABLE recherche (
    id INT REFERENCES trajet(id),
    email TEXT REFERENCES profil(email),
    heure_depart TIME, 
    ville_depart TEXT, 
    ville_arrivee TEXT, 
    numero_train INT, 
    heure_arrivee TIME, 
    disponibilite_max TEXT,
    CONSTRAINT pk_recherche PRIMARY KEY(id, email)
    );



"""
INSERT INTO trajet(date, heure_depart, ville_depart, ville_arrivee, numero_train, heure_arrivee, disponibilite_max) VALUES
('02/03/2021','12:00:00' , 'BRUZ', 'RENNES', 105, '13:00:00', TRUE);

INSERT INTO profil(email, nom, prenom, mot_de_passe, civilite, date_de_naissance) VALUES
('jules@gmail.com', 'Jules', 'Lejas', 'mdp', 'H','02/03/2001');

INSERT INTO recherche(email, id) VALUES 
('jules@gmail.com', 1);
"""