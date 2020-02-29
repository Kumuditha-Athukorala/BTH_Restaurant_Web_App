import pymysql
from database import Database

database = Database()

class Booking:

    def saveTableBookingRecord(self,data):

        try:
            firstName = data.get('firstName')
            lastname = data.get('lastName')
            phone = data.get('phone')
            email = data.get('email')
            adult = data.get('adult')
            children = data.get('children')
            booking_date = data.get('booking_date')
            booking_time = data.get('booking_time')
            comment = data.get('comment')
            status = "0"

            btime = "0"+booking_time + ":00:00"
            cursor = database.getDatabaseConnection()
            booking = Booking()
            user_id = booking.getUserId(email)
            if(len(user_id) != 0):

                sqlQuery = "INSERT INTO booking (mobile_number,email_address,nop,noc,date,time,description,user_id, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s )"
                recordTuple = (phone, email,adult,children,booking_date,btime,comment,user_id,status,)

                cursor.execute(sqlQuery, recordTuple)
                result = database.commitDatabaseConnection().commit()
                print(result)
                return result
            else:
                return "Invalied Email...!"

        except:
            print("Database Error...!")
        finally:
             cursor.close()


    def getUserId(self,email):

        try:
            cursor = database.getDatabaseConnection()
            sql = "SELECT user_id FROM user WHERE email_address = %s"

            cursor.execute(sql,email)
            result = cursor.fetchall()
            print(result)

            return result

        except:
            print("Database Error...!")
        finally:
            cursor.close()

    def getAllBookings(self):
        try:

            conn = database.commitDatabaseConnection()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT * FROM booking b INNER JOIN user u ON b.user_id = u.user_id")
            resultSet = cursor.fetchall()
            print(type(resultSet))
            return resultSet

        except:
            print("Database Error...!")

        finally:
            cursor.close()



    def cancelBookingRecord(self,data):

        booking_id = data.get

        try:
            cursor = database.getDatabaseConnection()
            sqlQuery = "UPDATE booking SET status= 2 WHERE booking_id=%s"
            cursor.execute(sqlQuery,booking_id)
            result = database.commitDatabaseConnection().commit()
            print(result)
            return result

        except:
            print("Database Error...!")

        finally:
            cursor.close()

    def confirmBookingRecord(self, id):

        booking_id =id

        try:
            cursor = database.getDatabaseConnection()
            sqlQuery = "UPDATE booking SET status= 1 WHERE booking_id=%s"
            cursor.execute(sqlQuery, booking_id)
            result = database.commitDatabaseConnection().commit()
            print(result)
            return result

        except:
            print("Database Error...!")

        finally:
            cursor.close()

