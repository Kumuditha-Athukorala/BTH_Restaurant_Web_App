
from dao.Customer import Customer
from service.PasswordRecoveryService import PwBackUpEmail
from service.PasswordManagingService import PasswordED

customer = Customer()
bkp = PwBackUpEmail()
ped = PasswordED()
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
        key="SlkumatybjykkkkkhhLKI90"
        print("recover passsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")

        result = customer.getPassword(data)
        pw = result[0]['password']
        print(pw)
        dpw= ped.decode(key,pw)
        print(dpw)
        email = data.get('email')
        print(email)
        emlResponce = bkp.sendEmail(email,dpw)

        return emlResponce



