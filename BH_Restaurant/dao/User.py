import pymysql
from database import Database
import hashlib
from service.PasswordManagingService import PasswordED

psd = PasswordED()
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
            key = "SlkumatybjykkkkkhhLKI90"

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
            emptyList = []
            if len(result) != 0:
                checkresult = result[0]['password'] == psd.encode(key, pswd)
                if checkresult:
                    return result
            else:
                return emptyList
        except:
            print("Database Error...!")
            return emptyList
        finally:
            cursor.close()



    def updatePassword(self, data, id):
        try:
            key = "SlkumatybjykkkkkhhLKI90"
            userId = id
            email = data.get('username')
            password = data.get('password')
            generatedPassword = psd.encode(key,password)
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


