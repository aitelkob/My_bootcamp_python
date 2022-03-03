test = 2
cooking_lvl = 2
test2 = 2
try:
    a = int(input("Enter a positive Number: "))
    if not  a in {test2,test,cooking_lvl}:
        raise ValueError("it's not a positive number!")
except ValueError as ve:
    print(ve)

