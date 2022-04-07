"""
Simple Python App to demonstrate delpoyment using GKE
This app will run in one container and will connect
with MySQL database running as another container using service name
"""

from flask import Flask, request, render_template
from flask_mysqldb import MySQL 

app = Flask(__name__)


conn = ""

app.config['MYSQL_HOST'] = 'mysql-service.default'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'system'

mysql = MySQL(app)

@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    #if request.method == 'POST':
    #    name = request.form['name']
    #    age = request.form['age']
    #    cursor = mysql.connection.cursor()
    #    cursor.execute(''' le VALUES(%s,%s)''')
    #    mysql.connection.commit()
    #    cursor.close()
    #    return f"Done!!"
    
    if request.method == 'POST':
         cursor = mysql.connection.cursor()
         cursor.execute(''' SHOW DATABASES ''',(name,age))
         mysql.connection.commit()
         cursor.close()
         return f"Done!!"

 
app.run(host='0.0.0.0', port=5000)
