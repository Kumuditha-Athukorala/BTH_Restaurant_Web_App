from dao.User import User

user = User()
class UserService:

    def checkUserLogin(self,data):
        result = user.checkUserLogin(data)
        print(type(result))
        if len(result) == 1:
            return 1
        else:
            return 0