
class Recipe:
    def __init__(self, name= "Null", cooking_lvl = -1, cooking_time = -1,
                 ingredients = ["Null"], description = "", recipe_type = "Null"):
        try:
            self.name = name
            self.cooking_lvl = cooking_lvl
            self.cooking_time = cooking_time
            self.ingredients = ingredients
            self.description = description
            self.recipe_type = recipe_type
            if "Null" in {self.name,self.ingredients[0],self.recipe_type}:
                raise Exception("all variables should not be empty ")
            if -1 in {self.cooking_lvl, self.cooking_time}:
                raise Exception("all variables should not be empty ")
            if not self.cooking_lvl in range(1,6):
                raise Exception("cooking Lecvel shoud be between 1 and 5")
            if not isinstance(self.cooking_time,int):
                raise Exception("just Int Sorry")
            if not self.recipe_type in ["starter", "lunch", "dessert"]:
                raise Exception("recipe_type should be either starter or lunch or dessert")
        except (Exception,ValueError) as ve:
            print("error ==",ve)
    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt += "Name of Recipe is " + self.name + "\n"
        txt += "level to cook the recipe " + str(self.cooking_lvl) + "\n"
        txt += "list of all ingredients " +(' '.join(ingr for ingr in self.ingredients))+ "\n"
        if self.description:
            txt+= "description of the recipe " + self.description + "\n"
        txt += "Recipe Type " + self.recipe_type 
        return txt
