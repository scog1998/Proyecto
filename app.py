from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '0998803919Sl.'
app.config['MYSQL_BD'] = 'proyecto'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/iniciar')
def iniciarsesion():
    return render_template('iniciar.html')

@app.route('/crear')
def crearcuenta():
    return render_template('crear.html')

if __name__ == '__main__':
    app.run(port=3000, debug= True)