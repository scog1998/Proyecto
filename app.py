from flask import Flask, render_template, request, Response, session, flash, redirect, url_for
from flask_mysqldb import MySQL

from Modelos.modeluser import modeluser

from Modelos.entities.User import User
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '0998803919Sl.'
app.config['MYSQL_DB'] = 'proyecto'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['MYSQL_CONNECT_TIMEOUT'] = 10  # Aumenta este valor según sea necesario

mysql = MySQL(app)



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/iniciar')
def iniciarsesion():
    return render_template('iniciar.html')

@app.route('/principal', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Crear una instancia de User con los parámetros adecuados
        user = User(
            id_usuario=0, 
            nombre_usuario=None,  # Si no lo necesitas por ahora, puedes dejarlo como None
            correo=request.form['correo'], 
            contrasena=request.form['contrasena']
        )

        # Crear una instancia de modeluser
        user_model = modeluser()

        # Verificar el usuario en la base de datos
        logged_user = user_model.login(mysql, user)

        if logged_user is not None:
            if User.check_password(logged_user['contrasena'], user.contrasena):  # Verificación correcta de la contraseña
                return redirect(url_for('principal'))
            else:
                flash("Contraseña Incorrecta") 
                return render_template('iniciar.html')
        else:
            flash("Usuario Incorrecto") 
            return render_template('iniciar.html')
    
    return render_template('iniciar.html') 

    
@app.route('/crear')
def crearcuenta():
    return render_template('crear.html')


if __name__ == '__main__':
    app.run(port=3000, debug= True)