from flask import Flask, request, jsonify, Response, send_file
import mysql.connector
import sys
app = Flask(__name__)


#db_connection = mysql.connector.connect(
#    host="db",  # This should match the service name in your Docker Compose file
#    user="root",
#    password="patata",
#    database="granier",
#)

@app.route("/api/base", methods=['POST'])
def proc_data():
    #data = request.json  # Assuming the frontend sends JSON data
    print("avonxd", file=sys.stderr)
    try:
    #    print("avonxd2", file=sys.stderr)
    #    return send_file("fillpdf.py", attachment_filename='ohhey.pdf')
        return send_file('in/Programa2.pdf', mimetype='application/pdf', as_attachment=True, download_name='example.pdf')
    except Exception as e:
           print("avon2", file=sys.stderr)    
    #cursor = db_connection.cursor()
    # Perform database operations using the cursor
    #return "<p>puta</p>"
    #return jsonify({"message": "Data processed successfully"})
    #with open('in/Programa2.pdf', 'rb') as pdf_file:
      #  pdf_data = pdf_file.read()
    #print("avonxd2", file=sys.stderr)
    #response = Response(pdf_data, content_type='application/pdf')
    #response.headers['Content-Disposition'] = 'attachment; filename=example.pdf'
    #return response


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/testing")
def test():
    return "<p>This is a not test</p>"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)