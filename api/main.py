from flask import Flask, request, jsonify, Response, send_file, render_template, session, json, abort
from flask_cors import CORS
import mysql.connector
from classes.Songs import Song
from classes.Act import Act
from classes.objectInstances import Objects
from classes.Organization import Organization
from classes.Autoliquidation import Autoliquidation
from classes.Db import DB_conn
from csv_writer import CSVWriter
import sys
import os
import time
import io
import zipfile
import subprocess
from flask_session import Session

app = Flask(__name__, static_url_path='/htmls', static_folder='/usr/share/nginx/html',template_folder='htmls')
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route("/api/base", methods=['POST'])
def proc_data():
    # db_connection = DB_conn()
    # db_connection.connect()
    data = request.json
    print(data, file=sys.stderr)
    # print(data, file=sys.stderr)
    
    act = Act(
        number=data.get('Numero-event'),
        title=data.get('Titol'),
        local_name=data.get('Local'),
        city=data.get('Poblacio'),
        province=data.get('Provincia'),
        init_date=data.get('Data-Inici'),
        end_date=data.get('Data-Fi'),
        songs=[]  # Empty list to start with
    )

    # jsonsongs = json.loads(data)
    
    songs: Song
    for key, value in data.items():
    
        if key.startswith("Titol"):
        
            var_number = key[5:] 
            if key[5:].isdigit():
                songs = Song(
                    title=data.get('Titol'+var_number),
                    author=data.get('Autor'+var_number),
                    subtitle=data.get('Subtitol'+var_number),
                    orchestra=data.get('Orquestra'+var_number),
                    times=data.get('Vegades'+var_number)
                )
                act.add_song(songs)
    Org = Organization(act)
    orgpochamataro =  Organization([],"253053","SardanaMat","Orq Mataro","Ripoll","Mataro","Mataro","Barcelona","Alfonso","Crrer de Mataro","34080","mat@mail.com","6543490","2344535","23/11/2023","30/11/2023","67438787E")
    orgpocharipoll =  Organization([],"253053","SardanaRip","Orq Ripoll","Ripoll","Ripoll","Ripoll","Barcelona","Maria","Crrer de Ripoll","34980","rip@mail.com","6543490","2344535","23/11/2023","30/11/2023","29436584T")
    if 'mataro' == 'mataro':
        Org = orgpochamataro
    else: 
        Org = orgpocharipoll

    Org.add_act(act)    
    #aqui trucar a get session + bd pillar datos org i enchufarlos a una org
    #  cs3 = CSVWriter()
    cs3 = CSVWriter()
    cs3.collect_SGAE_data(Org, act)
    file_path1 = os.path.normpath(os.path.join(os.getcwd(),'in','CSVs','Programs',str(Org.name) +'.csv'))
    cs3.write_to_csv(file_path1)      

    time.sleep(2)

    try:
        result = subprocess.run(['python', "fillpdf_program.py", Org.name])
        # result = subprocess.run(['python', "fillxlsx.py", "Testing_Orchestra"])
    except Exception as e:
        print(f"Error executing the script: {e}")
   
    try:
        return send_file('out/Programs/'+Org.name+".pdf", mimetype='application/pdf', as_attachment=True, download_name='Programa.pdf')
    except Exception as e:
           print("liada", file=sys.stderr)
           return FileNotFoundError
#end def proc_data()

@app.route("/api/auto", methods=['POST'])
def proc_data5():
    # db_connection = DB_conn()
    # db_connection.connect()
    data = request.json
    
    print(data, file=sys.stderr)
   
    # accedir bd i pillar actes de org usuario cookie
     
    #song1 = Song("the second", "idk", "subtit", "testing","34")
    #song2 = Song("the first", "author1", "Subtit", "Testing", "30")
    #act = Act("1","Testing", "Test_name", "Barcelona", "Barcelona", "26/12/2023", "30/12/2023", [song1,song2])
    #song3 = Song("second", "autor2", "Subtit", "orch","34")
    song4 = Song("first", "autor1", "Subtit", "Orch", "30")
    act2 = Act("253053","SardAnual", "Mataró", "Mataró", "Barcelona", "28/12/2023", "28/12/2023", [song4])
    auto = Autoliquidation(
        audition_days=data.get('Dies'),
        audition_price=data.get('tarifa'),
        contest_days=data.get('Dies-concursos'),
        contest_price=data.get('Preu'),
        num_couplets=data.get('Nombre-cobles'),
        concert_days=data.get('Dies-aplecs'),
        concert_earnings=data.get('total-pagar'),#data.get('total-pagar'),
        acts=[act2]  # Empty list to start with shauria danar a la bd a mirar actes per jorgito puto no curra
    )

    Org =  Organization([act2],"1","SardanaMat","Orq Mataro","Mataró","Mataro","Mataro","Barcelona","Alfonso","Crrer de Mataro","34080","mat@mail.com","6543490","2344535","23/11/2023","30/11/2023","67438787E")
    #orgpocharipoll =  Organization([act2],"1","SardanaRip","Orq Ripoll","Ripoll","Ripoll","Ripoll","Barcelona","Maria","Crrer de Ripoll","34980","rip@mail.com","6543490","2344535","23/11/2023","30/11/2023","29436584T")
    #if data.get('orgui') == 'mataro':
       # Org = orgpochamataro
    #else: 
       # Org = orgpocharipoll
        
    csv_writer = CSVWriter()
    csv_writer.collect_XLSX_data(Org)
    file_path = 'output.csv'
    csv_writer.write_to_csv(file_path)

    cs2 = CSVWriter()
    cs2.collect_Autoliquidation_data(auto,Org)
    file_path2 = os.path.normpath(os.path.join(os.getcwd(),'in','CSVs','Autoliquidations',str(Org.name) +'.csv'))
    cs2.write_to_csv(file_path2)

    time.sleep(2)
    try:
        result = subprocess.run(['python', "fillpdf.py", Org.name])
        result = subprocess.run(['python', "fillxlsx.py", Org.name])
    except Exception as e:
        print(f"Error executing the script: {e}")
   

    folder_path = 'out/Autoliquidations'
    folder_path2 = 'out/XLSX'
    # Create a BytesIO object to store the zip file
    zip_buffer = io.BytesIO()

    # Create a ZipFile object
    with zipfile.ZipFile(zip_buffer, 'a', zipfile.ZIP_DEFLATED, False) as zip_file:
        # Add specific files to the zip file
        zip_file.write(os.path.join(folder_path, Org.name +"_Autoliquidacio"+'.pdf'), Org.name+"_Autoliquidacio"+'.pdf')
        zip_file.write(os.path.join(folder_path2, "SGAE_ResumAutoliquidacions_" + Org.name +'.xlsx'), "SGAE_ResumAutoliquidacions_"+Org.name+'.xlsx')

    # Set the BytesIO object position to the beginning
    zip_buffer.seek(0)

    try:
        return send_file(zip_buffer, download_name='files.zip', as_attachment=True)
    except Exception as e:
           print("liada", file=sys.stderr)
           return FileNotFoundError   
    

@app.route("/api/login", methods=['POST'])
def proc_data3():
    db_connection = DB_conn()
    db_connection.connect()
    data = request.json
    # result = db_connection.user_login(data.get('user'),data.get('pass'))
    db_connection.desconnect()
    if data.get('user') == 'collamataro@gmail.com':
        if data.get('pass') == 'admin':
            return "success"
        else: abort(403,"access forbidden")
        #return render_template('paginaprincipal.html')#, usuario_id = data.get('user'))  # Redirect to the dashboard on successful login
    else: 
        abort(403,"access forbidden")
        #return render_template('login.html', message='Invalid username or password')   

@app.route("/api/register", methods=['POST'])
def proc_data2():
    db_connection = DB_conn()
    db_connection.connect()
    data = request.json
    #result = DB_conn.user_login(data.get('user'),data.get('pass'))
    db_connection.desconnect()
    if data:
        return render_template('paginaprincipal.html')  # Redirect to the dashboard on successful login
    else:
        return render_template('../htmls/login.html', message='Invalid username or password')   

@app.route('/def')
def usuario_valido():
    return render_template('paginaprincipal.html')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/testing")
def test():
    return "<p>This is a not test</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)