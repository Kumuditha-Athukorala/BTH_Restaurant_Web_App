from dao.Booking import Booking

booking = Booking()
class TableBookingService:

    def saveTableBookingRecord(self, data):
        result = booking.saveTableBookingRecord(data)
        return result


    def getAllBookings(self):
        result = booking.getAllBookings()
        return result
