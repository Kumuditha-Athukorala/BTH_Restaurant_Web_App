import pymysql
from database import Database
from service.PasswordManagingService import  PasswordED
import hashlib

database = Database()
pwc = PasswordED()
class Customer:
    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.gender = ""
        self.contactNumber = ""
        self.address=""
        self.emailaddress=""
        self.password=""
        self.status = ""

    def getEmailAddress(self,data):

        try:
            enterdEmail = data.get('email')
            cursor = database.getDatabaseConnection()
            sqlQuery = "SELECT email_address FROM user WHERE email_address=%s"
            cursor.execute(sqlQuery, enterdEmail)
            result = cursor.fetchall()
            print(result)
            return result

        except:
            print("Database Error...!")

        finally:
            cursor.close()

    def saveCustomer(self,data):

        try:
            firstName = data.get('firstName')
            lastname = data.get('lastName')
            gender = data.get('gender')
            phone = data.get('phone')
            address = data.get('address')
            email = data.get('email')
            password = data.get('password')
            generatedPassword = hashlib.sha256(password.encode()).hexdigest()

            status = "1"

            cursor = database.getDatabaseConnection()
            sqlQuery = "INSERT INTO user (first_name,last_name,gender,contact_number,address,email_address,password,status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )"
            recordTuple = (firstName, lastname, gender, phone, address, email, generatedPassword, status)

            cursor.execute(sqlQuery, recordTuple)
            result = database.commitDatabaseConnection().commit()
            print(result)
            return result

        except:
            print("Database Error...!")

        finally:
            cursor.close()



    def changeUserStatus(self, userId):
        try:

            cursor = database.getDatabaseConnection()

            sqlQuery = "UPDATE user SET status= CASE WHEN status=1 THEN 0 WHEN status=0 THEN 1 END WHERE user_id=%s"
            cursor.execute(sqlQuery,userId)
            result = database.commitDatabaseConnection().commit()
            print(result)
            return result

        except:
            print("Database Error...!")

        finally:
            cursor.close()


    def updateCustomerDetails(self, data, id):
        try:

            userId = id
            firstName = data.get('firstName')
            lastname = data.get('lastName')
            gender = data.get('gender')
            phone = data.get('phone')
            address = data.get('address')

            db = Database()
            cursor = db.getDatabaseConnection()

            sqlQuery = "UPDATE user SET first_name=%s, last_name=%s, gender=%s, contact_number=%s, address=%s WHERE user_id = %s "
            recordTuple = (firstName,lastname,gender,phone,address,userId)
            cursor.execute(sqlQuery,recordTuple)
            result = db.commitDatabaseConnection().commit()
            print(result)
            return result

        except:
            print("Database Error...!")

        finally:
            cursor.close()


    def getPassword(self,data):
        try:
            enterdEmail = data.get('email')
            db = Database()
            conn = db.commitDatabaseConnection()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "SELECT password FROM user WHERE email_address=%s"
            cursor.execute(sqlQuery, enterdEmail)
            resultSet = cursor.fetchall()
            print(type(resultSet))
            return resultSet

        except:
            print("Database Error...!")

        finally:
            cursor.close()
            conn.close()


import base64

def encode(key, string):
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    return base64.urlsafe_b64encode(encoded_string)