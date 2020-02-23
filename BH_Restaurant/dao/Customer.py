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