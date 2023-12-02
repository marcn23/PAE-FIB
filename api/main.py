from flask import Flask, request, jsonify, Response, send_file, render_template
from flask_cors import CORS
import mysql.connector
from classes.Songs import Song
from classes.Act import Act
from classes.objectInstances import Objects
from classes.Organization import Organization
from classes.Db import DB
import sys
app = Flask(__name__, template_folder='../html')
CORS(app)


@app.route("/api/base", methods=['POST'])
def proc_data():
    db_connection = DB.connect()
    #cursor = db_connection.cursor()
    #data = request.form.to_dict()
    data = request.json
    #print(data, file=sys.stderr)
    #print(data.get('Titol'), file=sys.stderr)
    #sql = "INSERT INTO ballades (titol, autor, cobla) VALUES (%s,%s,%s)"
    #values = (data.get('Titol'),"autoridad","coblestone")
    #cursor.execute(sql, values)
    #cursor.execute("SHOW TABLES")

    # Fetch all the tables
    #tables = cursor.fetchall()

    # Print the list of tables
    #for table in tables:
      #  print(table[0],file=sys.stderr)
    #cursor.execute("SELECT * FROM ballades")
    #result = cursor.fetchall()
    #print(result,file=sys.stderr)
    
    #db_connection.commit()
    #cursor.close()
    #db_connection.close()

    try:
        return send_file('in/Programa2.pdf', mimetype='application/pdf', as_attachment=True, download_name='example.pdf')
    except Exception as e:
           print("liada", file=sys.stderr)

    """
    act = Act(
        title=data.get('titleAct'),
        event_number=data.get('event_number'),
        local_name=data.get('local_name'),
        order_number=data.get('order_number'),
        invoice_number=data.get('invoice_number'),
        city=data.get('city'),
        province=data.get('province'),
        liq_included=data.get('liq_included'),
        sheet_number=data.get('sheet_number'),
        title_number=data.get('title_number'),
        parts=data.get('parts'),
        area_tit=data.get('area_tit'),
        day=data.get('day'),
        month=data.get('month'),
        year=data.get('year'),
        init_date=data.get('init_date'),
        end_date=data.get('end_date'),
        songs=[]  # Empty list to start with
    )

    for x in data:
        songs = Song(
            title=data.get('titleSong'),
            author=data.get('authorSong'),
            subtitle=data.get('subtitleSong'),
            orchestra=data.get('orchestra'),
            times=data.get('timesSong')
        )
        act.add_song(songs)
    """
#end def proc_data()

   
@app.route("/api/login", methods=['POST'])
def proc_data():
    data = request.json
    result = DB.user_login(data.get('user'),data.get('pass'))
    if result:
        return render_template('paginaprincipal.html')  # Redirect to the dashboard on successful login
    else:
        return render_template('login.html', message='Invalid username or password')   



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/testing")
def test():
    return "<p>This is a not test</p>"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)