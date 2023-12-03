import sys
import mysql.connector
from mysql.connector.cursor import MySQLCursor
from classes.Organization import Organization
from classes.Act import Act
from classes.Songs import Song


class DB:
    # Establishes a connection with Database
    # Returns a MySQLConnection
    def connect() -> mysql.connector.MySQLConnection:
        db_conn = mysql.connector.connect(
            host="db",  # This should match the service name in your Docker Compose file
            user="root",
            password="patata",
            database="granier",
        )
        return db_conn

    # Registers a user (organization)
    def user_register(db_conn, org: Organization, username: str, password: str) -> int:
        cursor: MySQLCursor = db_conn.cursor()
        sql = "INSERT INTO users VALUES(%s,%s,%s,%s,%s,%s,%s,%i,%i,%s)"
        values = (username,
                  password,
                  org.mail,
                  org.representator_dni,
                  org.direction,
                  org.city,
                  org.province,
                  org.postal_code,
                  org.mobile,
                  org.sgae_code)
        cursor.execute(sql, values)
        result = cursor.fetchall()
        cursor.close()

    # Returns 1 if credentials are correct, 0 otherwise
    def user_login(db_conn, username: str, password: str) -> bool:
        cursor: MySQLCursor = db_conn.cursor()
        sql = "SELECT COUNT(*) FROM users WHERE username=%s AND password=%s"
        values = (username, password)
        cursor.execute(sql, values)
        
        result = cursor.fetchone()
        cursor.close()
        return result[0]
    
    # Registers an Act
    def add_event(db_conn, a: Act):
        cursor: MySQLCursor = db_conn.cursor()
        sql = "INSERT INTO events (tipus, data, h1, poblacio, provincia, lloc, lloc_mal_temps, nom_activitat, cobla1, IDEN, autor) "
        sql += "VALUES(%s,%s,%s,%s)"
        values = (a.title,
                  a.init_date,
                  "12:00",
                  a.city,
                  a.province,
                  "Plaça del Lleo",
                  "Poliesportiu",
                  "Sardanes",
                  "Edgar coblero",
                  a.number,
                  "Joaquim autor")
        
        cursor.execute(sql, values)
        result = cursor.fetchall()
        cursor.close()
        return result
    
    # Registers a Song (ballada)
    def add_song(db_conn, s: Song):
        cursor: MySQLCursor = db_conn.cursor()
        sql = "INSERT INTO songs (title, author, subtitle, orchestra) VALUES(%s,%s,%s,%s)"
        values = (s.title,
                  s.author,
                  s.subtitle,
                  s.orchestra)
        cursor.execute(sql, values)
        result = cursor.fetchall()
        cursor.close()
        return result
        
