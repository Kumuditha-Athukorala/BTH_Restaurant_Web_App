import pymysql
from database import Database

database = Database()

class Booking:

    def saveTableBookingRecord(self,data):

        try:
            db = Database()
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
            cursor = db.getDatabaseConnection()
            booking = Booking()
            user_id = booking.getUserId(email)
            if(len(user_id) != 0):

                sqlQuery = "INSERT INTO booking (mobile_number,email_address,nop,noc,date,time,description,user_id, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s )"
                recordTuple = (phone, email,adult,children,booking_date,btime,comment,user_id,status,)

                cursor.execute(sqlQuery, recordTuple)
                result = db.commitDatabaseConnection().commit()
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
            database = Database()
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




    def cancelBookingRecord(self,id):

        try:
            cursor = database.getDatabaseConnection()
            sqlQuery = "UPDATE booking SET status= 2 WHERE booking_id=%s"
            cursor.execute(sqlQuery,id)
            result = database.commitDatabaseConnection().commit()
            print(result)
            return result

        except:
            print("Database Error...!")

        finally:
            cursor.close()



    def confirmBookingRecord(self, id):

        try:
            cursor = database.getDatabaseConnection()
            sqlQuery = "UPDATE booking SET status= 1 WHERE booking_id=%s"
            cursor.execute(sqlQuery, id)
            result = database.commitDatabaseConnection().commit()
            print(result)
            return result

        except:
            print("Database Error...!")

        finally:
            cursor.close()


    def getMyBookings(self,id):

        try:
            db = Database()
            userId = str(id)
            dbconn = db.commitDatabaseConnection()
            cursor = dbconn.cursor(pymysql.cursors.DictCursor)
            sql = "SELECT * FROM booking WHERE user_id = %s "
            cursor.execute(sql, userId)
            resultSet = cursor.fetchall()
            print(type(resultSet))
            return resultSet

        except:
            print("Database Error...!")

        finally:
            cursor.close()
            dbconn.close()




