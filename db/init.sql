
CREATE TABLE users (
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
    FOREIGN KEY (id_act) REFERENCES acts(id),
    FOREIGN KEY (id_song) REFERENCES songs(id)
);

INSERT INTO users (name, username, password, mail, representator_dni, representator_name, direction, city, province, postal_code, mobile, sgae_code)
VALUES
  ('Ciutat Amposta', 'Ciutat Amposta', 'hashed_password', 'joan@example.com', 12345678, 'Representant1', 'Carrer Principal 123', 'Barcelona', 'Barcelona', '08001', 123456789, 'SGAE123'),
  ('Berga Jove', 'Berga Jove', 'hashed_password', 'maria@example.com', 87654321, 'Representant2', 'Avinguda Secundària 456', 'Girona', 'Girona', '17001', 987654321, 'SGAE456'),
  ('Catània', 'Catània', 'hashed_password', 'miquel@example.com', 23456789, 'Representant3', 'Plaça Major 789', 'Tarragona', 'Tarragona', '43001', 234567890, 'SGAE789'),
  ('Cobla Catalana dels Sons Essencials', 'Cobla Catalana dels Sons Essencials', 'hashed_password', 'anna@example.com', 34567890, 'Representant4', 'Carrer Nou 567', 'Lleida', 'Lleida', '25001', 345678901, 'SGAE567'),
  ('Cobla Mataro', 'coblamataro', 'hashed_password', 'oriol@example.com', 45678901, 'Representant5', 'Passeig Marítim 123', 'Badalona', 'Barcelona', '08912', 456789012, 'SGAE890');

INSERT INTO songs (title, author, subtitle, orchestra, times)
VALUES
  ('50 anys a Taradell', 'Armenter i Ramos, Xavier', 'Subtítol1', 'Orquestra1', 23),
  ('50 anys amb el músic solitari', 'Paulí i Safont, Jordi', 'Subtítol2', 'Orquestra2', 134),
  ('50 anys amb tu', 'Galbany i Abril, Sigfrid', 'Subtítol3', 'Orquestra2', 87),
  ('50 anys ballant a la Platja', 'Puig i Fornis, Joan', 'Subtítol4', 'Orquestra3', 55),
  ('50 anys d''Agrupació a Bellpuig', 'Saladrigues i Solé, Antoni', 'Subtítol5', 'Orquestra2', 103),
  ('50 anys d''Amunt i Crits', 'Santiago i Roig, Carles', 'Subtítol6', 'Orquestra2', 76),
  ('50 anys d''aplecs', 'Xandrich i Crosas, Eduard', 'Subtítol7', 'Orquestra3', 34),
  ('50 anys d''aplecs gironins', 'Mas i Bou, Antoni', 'Subtítol8', 'Orquestra1', 98),
  ('50 anys de bàsquet a Palamós', 'Cuadrado i Alguacil, Amadeu', 'Subtítol9', 'Orquestra1', 12),
  ('50 anys de Dansaire', 'López i Serra, Jordi', 'Subtítol10', 'Orquestra1', 167),
  ('50 anys de joia', 'Font i Coll, Martirià', 'Subtítol11', 'Orquestra1', 45),
  ('50 anys de joia', 'Buscarons i Pastells, Lluís', 'Subtítol12', 'Orquestra3', 79),
  ('50 anys de mans enllaçades', 'Cassú i Serra, Josep', 'Subtítol13', 'Orquestra3', 8),
  ('50 anys de passió', 'Picamal i Coma, René', 'Subtítol14', 'Orquestra3', 112),
  ('50 anys de sardanes a Torregrossa', 'Prenafeta i Gavaldà, Josep', 'Subtítol15', 'Orquestra3', 90),
  ('50 anys de somnis', 'Gil i Membrado, Tomàs', 'Subtítol16', 'Orquestra1', 23),
  ('50 anys història', 'Santiago i Roig, Carles', 'Subtítol17', 'Orquestra3', 156),
  ('50 anys Unió', 'Alcalà i Baqués, Lluís', 'Subtítol18', 'Orquestra1', 42),
  ('50 anys en dansa', 'Cristau i Brunet, Jaume', 'Subtítol19', 'Orquestra3', 189),
  ('50 anys fent amics', 'Iglésias i Rodríguez, Ramon', 'Subtítol20', 'Orquestra1', 67),
  ('50 anys fent camí', 'Beumala i Sampons, Joan Jordi', 'Subtítol21', 'Orquestra1', 23),
  ('50 anys gaudint', 'Font i Turon, Albert', 'Subtítol22', 'Orquestra2', 178),
  ('50 anys i els que vindran', 'Fecúndez i Martínez, Josep', 'Subtítol23', 'Orquestra1', 33),
  ('50 anys i seguim', 'Planàs i Marca, Antoni', 'Subtítol24', 'Orquestra4', 144),
  ('50 anys i seguim!', 'Joanals i Ametller, Ivan', 'Subtítol25', 'Orquestra1', 76),
  ('50 anys, 9 colles', 'Gasulla i Porta, Daniel', 'Subtítol26', 'Orquestra1', 11),
  ('50 aplecs a Gràcia', 'Paulí i Safont, Jordi', 'Subtítol27', 'Orquestra5', 189),
  ('50 aplecs.. déu hi do!', 'Farràs i Casòliva, Josep', 'Subtítol28', 'Orquestra4', 52),
  ('50 històries per explicar', 'Abad i Gils, Anna', 'Subtítol29', 'Orquestra4', 132),
  ('50 i endavant!', 'Pujolar i Giménez, Montserrat', 'Subtítol30', 'Orquestra4', 98);

INSERT INTO acts (id, tipus, data, h1, h2, h3, poblacio, provincia, lloc, lloc_mal_temps, agrupacio, nom_activitat, mes_dades, cobla1, cobla2, cobla3, canvis, IDEN, link_programa, autor, data_creacio, data_canvis, comentaris, font1_tipus, font1_direccio)
VALUES
  (9, 'Ballada', '2023-09-15', '19:30:00', '21:30:00', '22:30:00', 'Vilafranca del Penedès', 'Barcelona', 'Plaça de Sant Jaume', 'Plaça de la Vila', 'Cobla Vilafranquina', 'Festa de la Verema', 'Més dades sobre la festa', 'Cobla Novena', 'Cobla Desena', NULL, 'Canvis en el repertori', 90123, 'https://exemple.com/programa9', 'Autor9', '2023-09-10 11:30:00', NULL, 'Comentaris sobre la festa', 'Font9', 'Direcció Font9'),
  (10, 'Concert', '2023-10-20', '20:00:00', '22:00:00', '23:00:00', 'Terrassa', 'Barcelona', 'Auditori Terrassa', 'Auditori Alternatiu', 'Orquestra Terrassenca', 'Concert Automne', 'Més dades sobre el concert', 'Cobla Deuena', 'Cobla Onzena', 'Cobla de Suport', 'Canvis en el programa', 12345, 'https://exemple.com/programa10', 'Autor10', '2023-10-15 09:30:00', '2023-10-18 17:00:00', 'Comentaris sobre el concert', 'Font10', 'Direcció Font10'),
  (11, 'Ballada', '2023-09-15', '19:30:00', '21:30:00', '22:30:00', 'Tortosa', 'Tarragona', 'Plaça del Castell', 'Plaça Major', 'Cobla Tortosina', 'Festa de la Tardor', 'Més dades sobre la festa', 'Cobla Onzena', 'Cobla Dotzena', NULL, 'Canvis en el repertori', 23456, 'https://exemple.com/programa11', 'Autor11', '2023-11-10 12:30:00', NULL, 'Comentaris sobre la festa', 'Font11', 'Direcció Font11'),
  (12, 'Concert', '2023-12-20', '19:00:00', '21:00:00', '22:00:00', 'Igualada', 'Barcelona', 'Teatre Igualadí', 'Teatre Alternatiu', 'Orquestra Igualadina', 'Concert de Nadal', 'Més dades sobre el concert', 'Cobla Dotzena', 'Cobla Tretzena', 'Cobla de Suport', 'Canvis en el programa', 34567, 'https://exemple.com/programa12', 'Autor12', '2023-12-15 10:00:00', '2023-12-18 18:00:00', 'Comentaris sobre el concert', 'Font12', 'Direcció Font12'),
  (13, 'Ballada', '2024-01-7', '20:00:00', '22:00:00', '23:00:00', 'Manlleu', 'Barcelona', 'Plaça Fra Bernadí', 'Plaça del Mercadal', 'Cobla Manlleuenca', 'Festa de Sant Antoni', 'Més dades sobre la festa', 'Cobla Tretzena', 'Cobla Catorzena', NULL, 'Canvis en el repertori', 45678, 'https://exemple.com/programa13', 'Autor13', '2024-01-10 12:00:00', NULL, 'Comentaris sobre la festa', 'Font13', 'Direcció Font13'),
    (14, 'Ballada', '2023-09-16', '19:30:00', '21:30:00', '22:30:00', 'Vilafranca del Penedès', 'Barcelona', 'Plaça de Sant Jaume', 'Plaça de la Vila', 'Cobla Vilafranquina', 'Festa de la Verema', 'Més dades sobre la festa', 'Cobla Novena', 'Cobla Desena', NULL, 'Canvis en el repertori', 99021, 'https://exemple.com/programa9', 'Autor9', '2023-09-10 11:30:00', NULL, 'Comentaris sobre la festa', 'Font9', 'Direcció Font9'),
  (15, 'Concert', '2023-12-22', '20:00:00', '22:00:00', '23:00:00', 'Terrassa', 'Barcelona', 'Auditori Terrassa', 'Auditori Alternatiu', 'Orquestra Terrassenca', 'Concert Automne', 'Més dades sobre el concert', 'Cobla Deuena', 'Cobla Onzena', 'Cobla de Suport', 'Canvis en el programa', 12341, 'https://exemple.com/programa10', 'Autor10', '2023-10-15 09:30:00', '2023-10-18 17:00:00', 'Comentaris sobre el concert', 'Font10', 'Direcció Font10'),
  (16, 'Ballada', '2023-11-17', '19:30:00', '21:30:00', '22:30:00', 'Tortosa', 'Tarragona', 'Plaça del Castell', 'Plaça Major', 'Cobla Tortosina', 'Festa de la Tardor', 'Més dades sobre la festa', 'Cobla Onzena', 'Cobla Dotzena', NULL, 'Canvis en el repertori', 23455, 'https://exemple.com/programa11', 'Autor11', '2023-11-10 12:30:00', NULL, 'Comentaris sobre la festa', 'Font11', 'Direcció Font11'),
  (17, 'Concert', '2023-12-25', '19:00:00', '21:00:00', '22:00:00', 'Igualada', 'Barcelona', 'Teatre Igualadí', 'Teatre Alternatiu', 'Orquestra Igualadina', 'Concert de Nadal', 'Més dades sobre el concert', 'Cobla Dotzena', 'Cobla Tretzena', 'Cobla de Suport', 'Canvis en el programa', 34588, 'https://exemple.com/programa12', 'Autor12', '2023-12-15 10:00:00', '2023-12-18 18:00:00', 'Comentaris sobre el concert', 'Font12', 'Direcció Font12'),
  (18, 'Ballada', '2024-01-3', '20:00:00', '22:00:00', '23:00:00', 'Manlleu', 'Barcelona', 'Plaça Fra Bernadí', 'Plaça del Mercadal', 'Cobla Manlleuenca', 'Festa de Sant Antoni', 'Més dades sobre la festa', 'Cobla Tretzena', 'Cobla Catorzena', NULL, 'Canvis en el repertori', 45610, 'https://exemple.com/programa13', 'Autor13', '2024-01-10 12:00:00', NULL, 'Comentaris sobre la festa', 'Font13', 'Direcció Font13');
 
INSERT INTO acts_songs (id_act, id_song)
VALUES
  (9, 6),  
  (9, 1),  
  (10, 1), 
  (10, 4), 
  (11, 4), 
  (11, 5), 
  (12, 5), 
  (12, 2),  
  (13, 2),  
  (13, 3), 
    (14, 5), 
  (15, 5), 
  (16, 2),  
  (17, 2),  
  (18, 3); 


