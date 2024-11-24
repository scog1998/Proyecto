from flask import Flask, render_template, request, Response, session
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

@app.route('/acceso-login', methods=["GET", "POST"])
def acceso():
    if request.method == 'POST' and 'correo' in request.form and 'contraseña':
        _email = request.form['correo']
        _password = request.form['contraseña']

        cur=mysql.connection.cursor
        cur.execute('SELECT * FROM usuarios WHERE correo = %s AND contasena = %s',(_email,_password))
        account = cur.fetchone()

        if account:
            session['logeado'] = True
            session['id_usuario'] = account['id_usuario']
            return render_template('acceso-login.html')
        else:

            return render_template('iniciar.html', mensaje="Usuario Incorecto")

if __name__ == '__main__':
    app.run(port=3000, debug= True)