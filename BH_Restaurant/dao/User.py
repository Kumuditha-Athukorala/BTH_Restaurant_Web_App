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
            cursor = database.getDatabaseConnection()
            cursor.execute("SELECT * FROM user")
            resultSet = cursor.fetchall()

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


