def text_analyzer(*text):
    """This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text."""
    if (len(text) > 1):
        print("ERROR")
    else:
        if (len(text) == 0):
            s = input("What is the text to analyse?")
        else:
            s = text[0]
        upper_count = 0
        lower_count = 0
        punct_count = 0
        space_count = 0
        char_count = 0
        for letter in s:
            char_count += 1
            if letter.isupper():
                upper_count += 1
            if letter.islower():
                lower_count += 1
            if letter == " ":
                space_count += 1
            if letter in ('!', ",", "\'", ";", "\"", ".", "-", "?"):
                punct_count += 1

        print('The text contains {} characters:'.format(char_count))
        print('- {} upper letters '.format(upper_count))
        print('- {} lower'.format(lower_count))
        print('- {} punctuation marks'.format(punct_count))
        print('- {} spaces'.format(space_count))
