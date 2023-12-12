
/*CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password CHAR(128) NOT NULL,
    mail VARCHAR(100) UNIQUE NOT NULL,
    representator_dni INT(8) UNIQUE NOT NULL,
    representator_name VARCHAR(128) NOT NULL,
    direction VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    province VARCHAR(255) NOT NULL,
    postal_code VARCHAR(6) NOT NULL,
    mobile INT(9) NOT NULL,
    sgae_code VARCHAR(10) UNIQUE NOT NULL
);

CREATE TABLE acts (
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
    IDEN INT(10) UNIQUE NOT NULL,
    link_programa VARCHAR(1024),
    autor VARCHAR(255) NOT NULL,
    data_creacio TIMESTAMP NOT NULL,
    data_canvis TIMESTAMP,
    comentaris VARCHAR(1024),
    font1_tipus VARCHAR(255),
    font1_direccio VARCHAR(255)
);

CREATE TABLE songs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(128) NOT NULL,
    subtitle VARCHAR(255) DEFAULT "",
    orchestra VARCHAR(255) NOT NULL,
    times INT(10) DEFAULT 0,
    CONSTRAINT id_attibutes UNIQUE (title, author, orchestra)
);

CREATE TABLE acts_songs (
    id_relation INT AUTO_INCREMENT PRIMARY KEY,
    id_act INT NOT NULL,
    id_song INT NOT NULL,
    FOREIGN KEY (id_act) REFERENCES events(id),
    FOREIGN KEY (id_song) REFERENCES songs(id)
);*/