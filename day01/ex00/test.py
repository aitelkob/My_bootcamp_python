from recipe import Recipe
from book import Book
import time

if __name__ == '__main__':
    # Create Recipe :
    listy = ['Pate', 'Saumon', 'Epinard']
    tourte = Recipe("Tourte", 3, 20, listy, "", "lunch")

    # Create second Recipe :
    listy = ['Miel', 'Banane', 'Yaourt']
    smoothie = Recipe("Smoothie miel-banane", 3, 10, listy,
            "Un smoothie de yaourt au miel et à la banane", "dessert")

    # Create Book :
    first_book = Book("First book")

    ### Testing :
    # Add Recipe to Book
    
    #first_book.add_recipe(tourte)
    #first_book.add_recipe(smoothie)
    # Add invalid Recipe to Book :
    # Book.add_recipe(first_book, 6)
    b = Book("My seductive recipes")
    print(b.creation_date)
    # should be the current date and time
    print(b.last_update)
    time.sleep(1.2)
    print("exampple ==============1 \n")
    crumble = Recipe("Crumble" , 1, 25, ["apples", "flour", "sugar"], "dessert" ,"delicious")
    b.add_recipe(crumble)
    print(b.last_update)
    # should be the same as the creation date or None
    # Find recipes in Book by type :
    #Book.get_recipes_by_types(first_book, 'lunch')
    #print("")

    # Print recipe from Book :
    #print(smoothie)
