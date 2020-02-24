from flask import session
from dao.User import User

user = User()
class UserService:

    def checkUserLogin(self,data):

        result = user.checkUserLogin(data)
        if len(result) == 1:
            for row in result:
                session["user"] = row[1]
            return 1
        else:
            return 0