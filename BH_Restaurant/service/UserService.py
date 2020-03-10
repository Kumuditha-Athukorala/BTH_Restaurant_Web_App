from flask import session
from dao.User import User


user = User()
class UserService:

    def checkUserLogin(self,data):

        result = user.checkUserLogin(data)
        if len(result) == 1:

            session["user"] = result[0]['first_name']
            session["userId"] = result[0]['user_id']
            session["email"] = result[0]['email_address']

            return 1
        else:
            return 0


    def allCustomers(self):
        result = user.getAllCustomers()
        return result


    def changePassword(self,data,id):

        result = user.updatePassword(data,id)
        return result

