import datetime
from recipe import Recipe

class Book:
    def __init__(self,name):
        self.name = name
        self.last_update = datetime.datetime.now()
        self.creation_date = datetime.datetime.now()
        self.creation_list = {'starter': [], 'lunch': [], 'dessert': []}
    def get_recipe_by_name(self, name):
        try:
            for lst in self.creation_list.values():
                for recip in lst:
                    if recip.name == name:
                        print(recip)
                        return (recip)
                else:
                    raise Exception("Couldn't find the recipe")
                            
        except (Exception,ValueError) as err:
               print("Error: " ,err)



