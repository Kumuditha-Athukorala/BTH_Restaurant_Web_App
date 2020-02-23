import pymysql

class Database:

    def __init__(self):
        try:
           self.connection = pymysql.connect(host='localhost', port=3307, user='root', password='1234', db='bt_house')
        except:
            print("Database Connection Error..!")

    def getDatabaseConnection(self):
        try:
           cursor = self.connection.cursor()
           return cursor;
        except:
            print("Database Connection Error..!")

    def commitDatabaseConnection(self):
        try:
            return self.connection
        except:
            print("Database Connection Error..!")

