from dao.Category import Category

cat = Category()
class CategoryService:

    def saveFoodCategory(self,data):
        result = cat.saveCategory(data)
        return result