from flask import Flask, request, jsonify
import mysql.connector
app = Flask(__name__)


db_connection = mysql.connector.connect(
    host="db",  # This should match the service name in your Docker Compose file
    user="root",
    password="patata",
    database="granier",
)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/testing")
def test():
    return "<p>This is a test</p>"

@app.route('/base', methods=['POST'])
def process_frontend_data():
    data = request.json  # Assuming the frontend sends JSON data

    cursor = db_connection.cursor()
    # Perform database operations using the cursor
    return "<p>puta</p>"
    #return jsonify({"message": "Data processed successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)