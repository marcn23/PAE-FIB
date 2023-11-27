
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password CHAR(128) NOT NULL,
    correu VARCHAR(100) UNIQUE NOT NULL,
    nif INT(8) UNIQUE NOT NULL,
    domicili VARCHAR(255) NOT NULL,
    domicili_num INT(4) NOT NULL,
    poblacio VARCHAR(255) NOT NULL,
    provincia VARCHAR(255) NOT NULL,
    codi_postal VARCHAR(6) NOT NULL,
    telefon INT(9) NOT NULL,
    codi_sgae VARCHAR(10)
);

CREATE TABLE events (
    id INT(10) NOT NULL PRIMARY KEY,
    tipus VARCHAR(255),
    data DATE NOT NULL,
    h1 TIME NOT NULL,
    h2 TIME,
    h3 TIME,
    poblacio VARCHAR(255) NOT NULL,
    provincia VARCHAR(255) NOT NULL,
    lloc VARCHAR(255) NOT NULL,
    lloc_mal_temps VARCHAR(255),
    agrupacio VARCHAR(255) NOT NULL,
    nom_activitat VARCHAR(255) NOT NULL,
    mes_dades VARCHAR(255),
    cobla1 VARCHAR(255) NOT NULL,
    cobla2 VARCHAR(255),
    cobla3 VARCHAR(255),
    canvis VARCHAR(255),
    IDEN INT(10) NOT NULL,
    link_programa VARCHAR(1024),
    autor VARCHAR(255) NOT NULL,
    data_creacio TIMESTAMP NOT NULL,
    data_canvis TIMESTAMP,
    comentaris VARCHAR(1024),
    font1_tipus VARCHAR(255),
    font1_direccio VARCHAR(255)
);

CREATE TABLE ballades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titol VARCHAR(255) PRIMARY KEY,
    autor VARCHAR(128) PRIMARY KEY,
    subtitol VARCHAR(255) DEFAULT "",
    cobla VARCHAR(255) PRIMARY KEY,
    vegades INT(10) DEFAULT 0,
    CONSTRAINT atributs_identificatius UNIQUE (titol, autor, cobla)
);

CREATE TABLE events_ballades (
    id_relacio INT AUTO_INCREMENT PRIMARY KEY,
    id_acte INT NOT NULL,
    id_ballada INT NOT NULL,
    FOREIGN KEY (id_acte) REFERENCES events(id),
    FOREIGN KEY (id_ballada) REFERENCES ballades(id)
);