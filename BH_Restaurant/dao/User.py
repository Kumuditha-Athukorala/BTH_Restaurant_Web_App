import pymysql
from database import Database


class User:
    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.gender = ""
        self.contactNumber = ""
        self.address=""
        self.emailaddress=""
        self.password=""
        self.status = 0

    def getAllCustomers(self):

        try:
            database = Database()
            conn = database.commitDatabaseConnection()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT * FROM user")
            resultSet = cursor.fetchall()
            print(type(resultSet))
            return resultSet

        except:
            print("Database Error...!")

        finally:
            cursor.close()
            conn.close()

    def checkUserLogin(self,data):

        try:
            database = Database()
            cursor = database.getDatabaseConnection()

            uname = data.get('username')
            pswd  = data.get('password')
            status = '1'

            print(uname)
            print(type(uname))

            sql_query = "SELECT * FROM user WHERE email_address = %s and password = %s and status =%s"
            cursor.execute(sql_query,(uname,pswd,status,))
            result = cursor.fetchall()

            return result

        except:
            print("Database Error...!")

        finally:
            cursor.close()



    def updatePassword(self, data, id):
        try:

            userId = id
            email = data.get('username')
            password = data.get('password')

            db = Database()
            cursor = db.getDatabaseConnection()

            sqlQuery = "UPDATE user SET password=%s WHERE user_id = %s AND email_address=%s "
            recordTuple = (password,userId,email)
            cursor.execute(sqlQuery,recordTuple)
            result = db.commitDatabaseConnection().commit()
            print(result)
            return result

        except:
            print("Database Error...!")

        finally:
            cursor.close()

