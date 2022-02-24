import sys


dict_code = { 'A':'.-', 'B':'-...',
             'C':'-.-.', 'D':'-..', 'E':'.',
             'F':'..-.', 'G':'--.', 'H':'....',
             'I':'..', 'J':'.---', 'K':'-.-',
             'L':'.-..', 'M':'--', 'N':'-.',
             'O':'---', 'P':'.--.', 'Q':'--.-',
             'R':'.-.', 'S':'...', 'T':'-',
             'U':'..-', 'V':'...-', 'W':'.--',
             'X':'-..-', 'Y':'-.--', 'Z':'--..',
             '1':'.----', '2':'..---', '3':'...--',
             '4':'....-', '5':'.....', '6':'-....',
             '7':'--...', '8':'---..', '9':'----.',
             '0':'-----', ', ':'--..--', '.':'.-.-.-',
             '?':'..--..', '/':'-..-.', '-':'-....-',
             '(':'-.--.', ')':'-.--.-'}


#chek_if char have == key in dict
def mourse(text):
    sentence = sys.argv[1].upper()
    mourse = ""
    for char in sentence:
        mourse+=dict_code[char] + " "
    return mourse
if len(sys.argv) > 1:
    str = sys.argv[1]
    for i in range(len(sys.argv) - 2):
        str = str + " " + sys.argv[i + 2]
    #mourse


print(mourse)
