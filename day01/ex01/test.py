
if __name__ == '__main__':
    arya = Stark("arya")
    print("Alive :", arya.is_alive)
    arya.die()
    print("Alive :", arya.is_alive)

    petyr = Baelish("Petyr")
    petyr.print_house_words()
