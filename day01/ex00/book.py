
class Book:
    def __init__(self,name, last_update,creation_date,recipes_list):
        self.name = name
        self.last_update = last_update
        self.creation_date = recipes_list


    def get_recipe_by_name(self,name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        pass
    
    def get_recipe_by_type(self,recipe_type):
        """Get all recipe names for a given recipe_type """
        pass

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        pass
