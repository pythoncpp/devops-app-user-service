import mysql.connector

class Database:

    def __init__(self):
        host = "db"
        user = "root"
        password = "root"
        database = "app_db"
        port = 3306
        self.__connection = mysql.connector.connect(host=host, user=user, password=password, database=database, port=port)

    def dcl(self, query):
        cursor = self.__connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        return data

    def dml(self, query):
        cursor = self.__connection.cursor()
        cursor.execute(query)
        cursor.close()
        self.__connection.commit()

    def __del__(self):
        self.__connection.close()