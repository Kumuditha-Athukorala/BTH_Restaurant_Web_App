from flask import session
from dao.User import User

user = User()
class UserService:

    def checkUserLogin(self,data):

        result = user.checkUserLogin(data)
        if len(result) == 1:
            for row in result:
                session["user"] = row[1]
                session["userId"] = row[0]
                session["email"] = row[6]
            return 1
        else:
            return 0


    def allCustomers(self):
        result = user.getAllCustomers()
        return result


    def changePassword(self,data,id):

        result = user.updatePassword(data,id)
        return result
