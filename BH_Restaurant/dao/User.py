import pymysql
from database import Database
import hashlib

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
            conn = database.commitDatabaseConnection()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            uname = data.get('username')
            pswd  = data.get('password')
            status = '1'


            query = "SELECT * FROM user WHERE email_address = %s and status=%s"
            cursor.execute(query, (uname,status))
            result = cursor.fetchall()
            print("DBBBBBBBBBBBBBBBBBBBBBBBBbb")
            print(type(result))
            print(result[0]['password'])
            print(result[0]['password'] == hashlib.sha256(pswd.encode()).hexdigest())

            checkresult = result[0]['password'] == hashlib.sha256(pswd.encode()).hexdigest()
            emptyList = []
            if len(result) != 0 and checkresult:
                return result
            elif len(result) != 0 and result[0]['password']== pswd:
                return result
            else:
                return emptyList
        except:
            print("Database Error...!")

        finally:
            cursor.close()



    def updatePassword(self, data, id):
        try:

            userId = id
            email = data.get('username')
            password = data.get('password')
            generatedPassword = hashlib.sha256(password.encode()).hexdigest()
            db = Database()
            cursor = db.getDatabaseConnection()

            sqlQuery = "UPDATE user SET password=%s WHERE user_id = %s AND email_address=%s "
            recordTuple = (generatedPassword,userId,email)
            cursor.execute(sqlQuery,recordTuple)
            result = db.commitDatabaseConnection().commit()
            print(result)
            return result

        except:
            print("Database Error...!")

        finally:
            cursor.close()


