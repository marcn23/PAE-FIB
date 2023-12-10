import sys
import mysql.connector
from mysql.connector.cursor import MySQLCursor
from classes.Organization import Organization
from classes.Act import Act
from classes.Songs import Song


class DB_conn:
    # Default constructor
    def __init__(self):
        self._host = "db"
        self._user = "root"
        self._password = "patata"
        self._database = "granier"
        self._conn = None
    
    
    # Open a DB connection
    def connect(self):
        try:
            self._conn = mysql.connector.connect(
                host = self._host,  # This should match the service name in your Docker Compose file
                user = self._user,
                password = self._password,
                database = self._database,
            )
        except mysql.connector.Error as err:
            print(f"Error de conexión: {err}")
            
        
    # Close a DB connection
    def desconnect(self):
        if self._conn:
            self._conn.close()
            print("Conexión cerrada")


    # Registers a user (organization)
    def user_register(self, org: Organization, username: str, password: str) -> int:
        cursor: MySQLCursor = self._conn.cursor()
        sql = "INSERT INTO users VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%i,%i,%s)"
        values = (org.name,
                  username,
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
        sql_result = cursor.fetchone()
        cursor.close()
        if sql_result is not None:
            return 0
        else:
            return sql_result


    # Returns 1 if credentials are correct, 0 otherwise
    def user_login(self, username: str, password: str) -> bool:
        cursor: MySQLCursor = self._conn.cursor()
        sql = "SELECT COUNT(*) FROM users WHERE username=%s AND password=%s"
        values = (username, password)
        cursor.execute(sql, values)
        sql_result = cursor.fetchone()
        cursor.close()
        return sql_result
    
    
    # Registers an Act to DB
    def add_act(self, a: Act):
        cursor: MySQLCursor = self._conn.cursor()
        sql = "INSERT INTO acts (tipus, data, h1, poblacio, provincia, lloc, lloc_mal_temps, nom_activitat, cobla1, IDEN, autor) "
        sql += "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%i,%s)"
        values = (a.title,
                  a.init_date,
                  "12:00",
                  a.city,
                  a.province,
                  "Plaça del Lleo",
                  "Poliesportiu",
                  "Sardanes",
                  "Cobla Edgar",
                  a.number,
                  "Joaquim autor")
        cursor.execute(sql, values)
        sql_result = cursor.fetchone()
        cursor.close()
        if sql_result is not None:
            return 0
        else:
            return sql_result

    
    # Registers a Song (ballada) to DB
    def add_song(self, s: Song):
        cursor: MySQLCursor = self._conn.cursor()
        sql = "INSERT INTO songs (title, author, subtitle, orchestra) VALUES(%s,%s,%s,%s)"
        values = (s.title,
                  s.author,
                  s.subtitle,
                  s.orchestra)
        cursor.execute(sql, values)
        result = cursor.fetchall()
        cursor.close()
        return result
        
        
    # Add a registered Song TO an Act
    def add_song2act(self, id_act: int, song: Song):
        cursor: MySQLCursor = self._conn.cursor()
        sql = "SELECT id FROM songs WHERE title=%s AND author=%s AND orchestra=%s"
        values = (song.title, song.author, song.orchestra)
        cursor.execute(sql, values)
        id_song = cursor.fetchone()
        
        sql = "INSERT INTO acts_songs (id_act, id_song) VALUES(%i,%i)"
        values = (id_act, id_song)
        cursor.execute(sql, values)
        result = cursor.fetchall()
        cursor.close()
        return result
    
    
    def get_organization(self, org_name: str) -> Organization:
        cursor: MySQLCursor = self._conn.cursor()
        sql = "SELECT * FROM users WHERE name=%s"
        values = (org_name)
        cursor.execute(sql, values)
        sql_org = cursor.fetchone()
        org = Organization(acts= [],
                           number= sql_org[0],
                           name= sql_org[1],
                           orchestra= sql_org[0],
                           place= "",
                           order_place= "",
                           city= sql_org[8],
                           province= sql_org[9],
                           representator_name= sql_org[6],
                           direction=sql_org[7],
                           postal_code= sql_org[10],
                           mail= sql_org[4],
                           mobile= sql_org[11],
                           sgae_code= sql_org[12],
                           initial_date= None,
                           final_date= None,
                           representator_dni= sql_org[5]
                           )
        
        sql = "SELECT * FROM acts WHERE agrupacio=%s"
        values = (org_name)
        cursor.execute(sql, values)
        sql_acts = cursor.fetchall()
        cursor.close()
        for a in sql_acts:
            org.add_act(self._get_act(a))
        return org
    
    
    def _get_act(self, sql_result) -> Act:
        cursor: MySQLCursor = self._conn.cursor()
        sql = "SELECT id_song FROM acts_songs WHERE id_act=%i"
        values = (sql_result[0])
        cursor.execute(sql, values)
        sql_songs = cursor.fetchall()
        act = Act(number = sql_result[0],
                  title = sql_result[11],
                  local_name = sql_result[8],
                  city = sql_result[6],
                  province = sql_result[7],
                  init_date = sql_result[2],
                  end_date = sql_result[2],
                  songs = []
                  )
        for song_id in sql_songs:
           act.add_song(self._get_song(song_id))
        return act    
        
    
    # Given a Song id, returns the instance of the Song
    def _get_song(self, id_song) -> Song:
        cursor: MySQLCursor = self._conn.cursor()
        sql = "SELECT title,author,subtitle,orchestra,times FROM songs WHERE id=%i"
        values = (id_song)
        cursor.execute(sql, values)
        sql_result = cursor.fetchone()
        return Song(title = sql_result[0],
                    author = sql_result[1],
                    subtitle = sql_result[2],
                    orchestra = sql_result[3],
                    times = sql_result[4]
                    )
