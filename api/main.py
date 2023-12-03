from flask import Flask, request, jsonify, Response, send_file, render_template, session, json
from flask_cors import CORS
import mysql.connector
from classes.Songs import Song
from classes.Act import Act
from classes.objectInstances import Objects
from classes.Organization import Organization
from classes.Autoliquidation import Autoliquidation
from classes.Db import DB
import sys
from flask_session import Session

app = Flask(__name__, template_folder='../htmls')
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route("/api/base", methods=['POST'])
def proc_data():
    db_connection = DB.connect()
    data = request.json
    
    #print(data, file=sys.stderr)
   

    
    act = Act(
        number=data.get('Numero-event'),
        title=data.get('Titol'),
        local_name=data.get('local_name'),
        city=data.get('Poblacio'),
        province=data.get('Provincia'),
        init_date=data.get('Data-inici'),
        end_date=data.get('Data-fi'),
        songs=[]  # Empty list to start with
    )

    jsonsongs = json.loads(data)

    songs: Song
    for key, value in jsonsongs.items():
    
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

    #aqui trucar a get session + bd pillar datos org i enchufarlos a una org      
    """
    csv_writer = CSVWriter()
    csv_writer.collect_XLSX_data(org)
    file_path = 'output.csv'
    csv_writer.write_to_csv(file_path)


    cs3 = CSVWriter()
    cs3.collect_SGAE_data(org, act)
    file_path1 = os.path.normpath(os.path.join(os.getcwd(),'in','CSVs','Programs',str(org.name) +'.csv'))
    cs3.write_to_csv(file_path1)

    time.sleep(2)
    try:
        result = subprocess.run(['python', "fillpdf_program.py", "Testing_Orchestra"])
        result = subprocess.run(['python', "fillxlsx.py", "Testing_Orchestra"])
    except Exception as e:
        print(f"Error executing the script: {e}")
    """   
    try:
        return send_file('in/Programs_Template.pdf', mimetype='application/pdf', as_attachment=True, download_name='example.pdf')
    except Exception as e:
           print("liada", file=sys.stderr)
           return FileNotFoundError
#end def proc_data()

@app.route("/api/auto", methods=['POST'])
def proc_data5():
    db_connection = DB.connect()
    data = request.json
    
    #print(data, file=sys.stderr)
   
    #accedir bd i pillar actes de org usuario cookie
     
    """
    auto = Autoliquidation(
        audition_days=data.get('Numero-event'),
        audition_price=data.get('Titol'),
        contest_days=data.get('local_name'),
        contest_price=data.get('Poblacio'),
        num_couplets=data.get('Provincia'),
        concert_days=data.get('Data-inici'),
        concert_earnings=data.get('Data-fi'),
        acts=[]  # Empty list to start with
    )


        
    
    csv_writer = CSVWriter()
    csv_writer.collect_XLSX_data(org)
    file_path = 'output.csv'
    csv_writer.write_to_csv(file_path)


    cs2 = CSVWriter()
    cs2.collect_Autoliquidation_data(autoliquidation,org)
    file_path2 = os.path.normpath(os.path.join(os.getcwd(),'in','CSVs','Autoliquidations',str(org.name) +'.csv'))
    cs2.write_to_csv(file_path2)

    time.sleep(2)
    try:
        result = subprocess.run(['python', "fillpdf_program.py", "Testing_Orchestra"])
        result = subprocess.run(['python', "fillxlsx.py", "Testing_Orchestra"])
    except Exception as e:
        print(f"Error executing the script: {e}")
    """   
    try:
        return send_file('in/Programs_Template.pdf', mimetype='application/pdf', as_attachment=True, download_name='example.pdf')
    except Exception as e:
           print("liada", file=sys.stderr)
           return FileNotFoundError   
    

@app.route("/api/login", methods=['POST'])
def proc_data3():
    db_connection = DB.connect()
    data = request.json
    result = DB.user_login(db_connection,data.get('user'),data.get('pass'))
    if result:

        return render_template('paginaprincipal.html', usuario_id = data.get('user'))  # Redirect to the dashboard on successful login
    else:
        return render_template('login.html', message='Invalid username or password')   

@app.route("/api/register", methods=['POST'])
def proc_data2():
    db_connection = DB.connect()
    data = request.json
    result = DB.user_login(db_connection,data.get('user'),data.get('pass'))
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