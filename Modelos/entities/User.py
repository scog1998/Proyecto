from werkzeug.security import check_password_hash

class User:
    def __init__(self, id_usuario, nombre_usuario, correo, contrasena):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.correo = correo
        self.contrasena = contrasena

    @classmethod
    def check_password(cls, hashed_password, password):
        return check_password_hash(hashed_password, password)  
