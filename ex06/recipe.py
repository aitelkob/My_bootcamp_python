import sys

def clr():
    print("\033c", end="")

cookbook = {
    "sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": "10",
    },
    "cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": "60",
    },
    "salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": "15",
    },
}


def print_recipe_from_cookbook(recipe):
    if recipe in cookbook.keys():
        print("Recipe for {}:".format(recipe))
        print("Ingredient list: {}".format(cookbook[recipe][0]))
        print("To be eaten for {}.".format(cookbook[recipe][1]))
        print("Takes {} minutes of cooking.".format(cookbook[recipe][2]))
    else:
        print("Invalid recipe name.")


def del_recipe(recipe):
    if recipe in cookbook.keys():
        cookbook.pop(recipe)
        print("Deleted {} recipe.".format(recipe))
    else:
        print("Invalid recipe name.")

def add_recipe(recipe,ingredients, meal ,prep_time):
    cookbook[recipe] = (ingredients, meal,prep_time)
    print(cookbook[recipe])
    print("Added '{}' to cookbook.".format(recipe))

def print_all_recipe():
    [print_recipe_from_cookbook(recipe) for recipe in cookbook.keys()]

def error_manage(choice):
    if (not choice.isdigit()):
        print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")
        return False
    else:
        return True
def menu(choice):
        clr()
        if choice == 1:
            name = input("Enter the name of the recipe you'd like to add: ")
            if name in cookbook.keys():
                print("'{}' already exists, overwriting...".format(name))
                return
            ingredients = input("Enter the ingredients in the format "
                            "'flour,sugar, eggs...': ").split(',')
            meal = input("Enter the type of meal (lunch, dessert...): ")
            time = input("Enter the recipe's prep time, in minutes: ")
            add_recipe(name, ingredients, meal, time)
        elif choice == 2:
            name = input("Enter the name of the recipe you'd like to delete: ")
            del_recipe(name)
        elif choice == 3:
            name = input("Please enter the recipe's name to get its details: ")
            print_recipe_from_cookbook(name)
        elif choice == 4:
            print_all_recipe()
        elif choice == 5:
            print("Cookbook closed.")
            exit()
        else:
            print("This option does not exist.")


while 1:
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit")
    choice = input(">>")
    if error_manage(choice):
        menu(int(choice))

