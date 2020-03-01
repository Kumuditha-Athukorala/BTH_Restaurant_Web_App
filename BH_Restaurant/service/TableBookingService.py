from dao.Booking import Booking

booking = Booking()
class TableBookingService:

    def saveTableBookingRecord(self, data):
        result = booking.saveTableBookingRecord(data)
        return result


    def getAllBookings(self):
        result = booking.getAllBookings()
        return result

    def processBookingOrder(self,status,id):
        print(status,id)
        if(status == "0"):
            booking.cancelBookingRecord(id)
        else:
            booking.confirmBookingRecord(id)

    def getMyBookingDetails(self, id):

        resultSet = booking.getMyBookings(id)
        return resultSet
