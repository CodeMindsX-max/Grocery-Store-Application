import mysql.connector
__cnx = None
def get_mysql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='34124390',
                                    host='127.0.0.1',
                                    database='gs')
    return __cnx