
CREATE TABLE events (
    Id INT(10) NOT NULL PRIMARY KEY,
    Tipus VARCHAR(255),
    Data DATE NOT NULL,
    H1 TIME NOT NULL,
    H2 TIME,
    H3 TIME,
    Poblacio VARCHAR(255) NOT NULL,
    Provinicia VARCHAR(255) NOT NULL,
    Lloc VARCHAR(255) NOT NULL,
    LlocMalTemps VARCHAR(255),
    Agrupacio VARCHAR(255) NOT NULL,
    NomActivitat VARCHAR(255) NOT NULL,
    MesDades VARCHAR(255),
    Cobla1 VARCHAR(255) NOT NULL,
    Cobla2 VARCHAR(255),
    Cobla3 VARCHAR(255),
    Canvis VARCHAR(255),
    IDEN INT(10) NOT NULL,
    LinkPrograma, VARCHAR(1024)
    Autor VARCHAR(255) NOT NULL,
    DataCreacio TIMESTAMP NOT NULL,
    DataCanvis TIMESTAMP,
    Comentaris VARCHAR(1024),
    Font1_Tipus VARCHAR(255),
    Font1_Direccio VARCHAR(255)
)

CREATE TABLE users (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(50) UNIQUE NOT NULL,
    Password CHAR(128) NOT NULL,
    Correu VARCHAR(100) UNIQUE NOT NULL,
    Nif INT(8) UNIQUE NOT NULL,
    Domicili VARCHAR(255) NOT NULL,
    DomiciliNum INT(4) NOT NULL
    Poblacio VARCHAR(255) NOT NULL,
    Provincia VARCHAR(255) NOT NULL,
    CodiPostal VARCHAR(6) NOT NULL,
    Telefon INT(9) NOT NULL,
    CodiSgae VARCHAR(10)
)