import sys

cookbook = {}

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
        del cookbook[recipe]
        print("Deleted {} recipe.".format(recipe))
    else:
        print("Invalid recipe name.")

def add_recipe(recipe,ingredients, meal ,prep_time):
    if recipe in cookbook.keys():
        print("'{}' already exists, overwriting...".format(recipe))
    cookbook[recipe] = (ingredients, meal.prep_time)
    print("Added '{}' to cookbook.".format(recipe))

def print_all_recipe():
    [print_recipe_from_cookbook(recipe) for recipe in cookbook.keys()]


chois = 0
