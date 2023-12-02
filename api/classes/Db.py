import sys
import mysql.connector
from mysql.connector.cursor import MySQLCursor
from classes.Organization import Organization


class DB:
    def connect() -> mysql.connector.MySQLConnection:
        db_conn = mysql.connector.connect(
            host="db",  # This should match the service name in your Docker Compose file
            user="root",
            password="patata",
            database="granier",
        )
        return db_conn

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
    
    def add_event():
        return 
        
        
