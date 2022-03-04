import datetime
from recipe import Recipe

class Book:
    def __init__(self,name):
        self.name = name
        self.last_update = datetime.datetime.now()
        self.creation_date = datetime.datetime.now()
        self.creation_list = {'starter': [], 'lunch': [], 'dessert': []}
    def __str__(self):
        txt = ("Recipe book's name : " + self.name + "\n"
            + "Last update : " + str(self.last_update) + "\n"
            + "Creation date : " + str(self.creation_date) + "\n"
            + "Starters : " + str(self.recipes_list['starter']) + "\n"
            + "Lunches : " + str(self.recipes_list['lunch']) + "\n"
            + "Desserts : " + str(self.recipes_list['dessert']))
    return txt
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
# first_book = Book("First book")
# Book.get_recipes_by_types(first_book, 'starter')

# print(first_book.name)
# print(first_book.last_update)
# print(first_book.creation_date)
# print(first_book.recipes_list)
