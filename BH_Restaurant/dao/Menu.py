import pymysql
from database import Database

database = Database()
class Menu:

    def saveMenuItem(self, data,img):
            try:
                    itemName = data.get('menuName')
                    category = data.get('m_cat')
                    price = data.get('price')
                    imgURL = img
                    description = data.get('des')
                    status = "1"

                    cursor = database.getDatabaseConnection()
                    sqlQuery = "INSERT INTO menu (menu_name,category_id,price,image, description,status) VALUES (%s, %s, %s, %s, %s,%s )"
                    recordTuple = (itemName, category, price, imgURL, description, status)

                    cursor.execute(sqlQuery, recordTuple)
                    result = database.commitDatabaseConnection().commit()
                    print(result)
                    return result
            except:
                    print("Databse Error...!")
            finally:
                    cursor.close()





    def getMenuList(self):

            try:
                    db = Database()
                    conn = db.commitDatabaseConnection()
                    cursor = conn.cursor(pymysql.cursors.DictCursor)
                    sqlQuery = "SELECT m.menu_id,m.menu_name,m.price,m.image,m.description,m.status,c.category_id,c.cat_name FROM menu m INNER JOIN category c ON m.category_id = c.category_id"
                    cursor.execute(sqlQuery)
                    result = cursor.fetchall()
                    print(result)
                    return result

            except:
                    print("Database Error...!")

            finally:
                    cursor.close()
                    conn.close()

