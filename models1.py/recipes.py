Class Recipe_category:

    def __init__(self,title):
        self.title = title
        self.recipes =[]

    def add_recipe(self, recipe):
        if recipe not in self.recipes:
            self.recipes.append(recipe)
            return "recipe added succesfully"
        return "recipe already exists"

    def edit_recipe(self,newrecipe,oldrecipe):
        if oldrecipe in self.recipes:
            self.recipes= [newrecipe for oldrecipe in self.recipes]
            return "recipe added successfully"
        return "no recipe to edit"

    def delete_recipe(self,recipe):
        if recipe in self.recipes:
            self.recipes.remove(recipe)
            return "recipe deleted"
        return "No recipe to delete"

    def view_recipe(self,recipe):
        for recipe in self.recipes:
            return self.recipes
        return "no recipe found"
