class Category:

    def __init__(self,title):
        self.title =title
        self.recipe_categories=[]

    def add_recipe_category(self,recipe_category):
        if recipe_category not in self.recipe_categories:
            self.recipe_categories.append(recipe_category)
            return "recipe category is added succesfully"
        return "recipe category already exists"

    def edit_recipe_category(self,newname,oldname):
        if oldname in self.recipe_categories:
            self.recipe_category =[newname for oldname  in self.recipe_categories]
            return "recipe_category edited succesfully"
        return "recipe_category not found"

    def delete_recipe_category(self,recipe_category):
        if recipe_category in self.recipe_categories:
            self.recipe_categories.remove(recipe_category)
            return "recipe_category deleted"
        return "recipe_category not found"


