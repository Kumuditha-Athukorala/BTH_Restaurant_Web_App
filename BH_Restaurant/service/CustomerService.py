from dao.Customer import Customer

customer = Customer()

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