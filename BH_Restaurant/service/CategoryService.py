from dao.Category import Category
from dao.Menu import  Menu

cat = Category()
menu = Menu()
class CategoryService:

    def saveFoodCategory(self,data):
        result = cat.saveCategory(data)
        return result

    def saveMenuItem(self,data,img):
        result = menu.saveMenuItem(data,img)
        return result

    def getAllCtegories(self):
        result = cat.allcategories()
        return result

    def getMenuItemsWithCategory(self):
        result = menu.getMenuList()
        return result