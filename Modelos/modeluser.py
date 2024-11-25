from .entities.User import User
class modeluser():
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id_usuario, nombre_usuario, correo, contrasena FROM usuarios WHERE correo = %s"
            cursor.execute(sql, (user.correo,))
            row=cursor.fetchone()
            print("Row:", row)
            if row != None:
                user = User(row[0], row[2], User.check_password(row[3], user.password), row[1])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)        
          
             