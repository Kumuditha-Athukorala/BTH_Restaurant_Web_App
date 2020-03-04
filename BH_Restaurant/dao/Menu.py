import pymysql
from database import Database

database = Database()
class Menu:

    def saveMenuItem(self, data,img):

            itemName = data.get('menuName')
            category = data.get('m_cat')
            price = data.get('price')
            imgURL = img
            description = data.get('des')
            status = "1"

            cursor = database.getDatabaseConnection()
            sqlQuery = "INSERT INTO menu (menu_name,category_id,price,image, description,status) VALUES (%s, %s, %s, %s, %s,%s )"
            recordTuple = (itemName,category,price,imgURL,description,status)

            cursor.execute(sqlQuery, recordTuple)
            result = database.commitDatabaseConnection().commit()
            print(result)
            return result
