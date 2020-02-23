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

    def getEmailAddress(self,data):

        enterdEmail = data.get('email')
        cursor = database.getDatabaseConnection()
        sqlQuery = "SELECT email_address FROM customer WHERE email_address=%s"
        cursor.execute(sqlQuery,enterdEmail)
        result = cursor.fetchall()
        print(result)

        return result

    def saveCustomer(self,data):

        firstName = data.get('firstName')
        lastname = data.get('lastName')
        gender = data.get('gender')
        phone = data.get('phone')
        address = data.get('address')
        email = data.get('email')
        password = data.get('password')

        cursor = database.getDatabaseConnection()
        sqlQuery = "INSERT INTO customer (first_name,last_name,gender,contact_number,address,email_address,password) VALUES (%s, %s, %s, %s, %s, %s, %s )"
        recordTuple = (firstName,lastname,gender,phone,address,email,password)

        cursor.execute(sqlQuery,recordTuple)
        result = database.commitDatabaseConnection().commit()
        print(result)
        return result
