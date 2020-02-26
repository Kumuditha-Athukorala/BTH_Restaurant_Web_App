from database import Database

database = Database()
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
            status = "1"

            cursor = database.getDatabaseConnection()
            sqlQuery = "INSERT INTO user (first_name,last_name,gender,contact_number,address,email_address,password,status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )"
            recordTuple = (firstName, lastname, gender, phone, address, email, password, status)

            cursor.execute(sqlQuery, recordTuple)
            result = database.commitDatabaseConnection().commit()
            print(result)
            return result

        except:
            print("Database Error...!")

        finally:
            cursor.close()


