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

        try:
            database = Database()
            cursor = database.getDatabaseConnection()
            cursor.execute("SELECT * FROM customer")
            resultSet = cursor.fetchall()
            cursor.close()
            return resultSet

        except:
            print("Database Error...!")

        finally:
            cursor.close()

    def checkUserLogin(self,data):

        try:
            database = Database()
            cursor = database.getDatabaseConnection()

            uname = data.get('username')
            pswd  = data.get('password')

            print(uname)
            print(type(uname))

            sql_query = "SELECT * FROM customer WHERE email_address = %s and password = %s"
            cursor.execute(sql_query,(uname,pswd,))
            result = cursor.fetchall()

            return result

        except:
            print("Database Error...!")

        finally:
            cursor.close()


