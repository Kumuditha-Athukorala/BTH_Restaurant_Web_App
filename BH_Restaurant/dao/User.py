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

    def getAllCustomers(self):
        database = Database()
        cursor = database.getDatabaseConnection()
        cursor.execute("SELECT * FROM customer")
        resultSet = cursor.fetchall()
        cursor.close()
        return resultSet

    def checkUserLogin(self,data):
        database = Database()
        cursor = database.getDatabaseConnection()

        uname = data.get('username')

        print(uname)
        print(type(uname))

        sql_query = "SELECT * FROM customer WHERE email_address=%s"
        cursor.execute(sql_query,uname)
        result = cursor.fetchall()
        print(result)
        return result
