class Config:
    SECRET_KEY = 'asd'

class ConfigBD(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '0998803919Sl.'
    MYSQL_BD = 'Proyecto'    

config = {
    'development': Config
}