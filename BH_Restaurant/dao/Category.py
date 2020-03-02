import pymysql
from database import Database

database = Database()
class Category:

    def saveCategory(self,data):

        try:
            catName = data.get('catName')

            cursor = database.getDatabaseConnection()
            sqlQuery = "INSERT INTO category (cat_name) VALUES (%s)"
            recordTuple = (catName)

            cursor.execute(sqlQuery, recordTuple)
            result = database.commitDatabaseConnection().commit()
            print(result)
            return result

        except:
            print("Database Error...!")

        finally:
            cursor.close()
