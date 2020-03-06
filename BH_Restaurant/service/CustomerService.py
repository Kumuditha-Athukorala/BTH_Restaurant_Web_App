
from dao.Customer import Customer
from service.PasswordRecoveryService import PwBackUpEmail

customer = Customer()
bkp = PwBackUpEmail()

class CustomerService:

    def checkCustomerEmail(self,data):
        result = customer.getEmailAddress(data)
        if len(result) == 1:
            return 1
        else:
            return 0

    def rgisterCustomer(self,data):
        result = customer.saveCustomer(data)
        print(result)
        return result

    def updateUserStatus(self,data):

        id = data.get('userId')
        result = customer.changeUserStatus(id)

        return result

    def updateCustomerDetails(self,data,id):

        result =customer.updateCustomerDetails(data,id)
        return result

    def recoverPassword(self, data):
        print("recover passsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")

        result = customer.getPassword(data)
        pw = result[0]['password']
        print(pw)
        print(result)
        print(type(result))
        email = data.get('email')
        print(email)
        emlResponce = bkp.sendEmail(email,pw)

        return emlResponce

