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

if len(sys.argv) < 1:
    print("ERROR")
    exit()
elif len(sys.argv) == 1:
    exit()
for c in sys.argv[1:]:
    if not c.replace(' ','').isalnum():
        print("ERROR")
        exit()
code = []
text = [string.upper() for string in sys.argv[1:]]
index = 0
for string in text:
    for char in string:
        if (char == ' '):
            code.append("/")
        else:
            code.append(dict_code[char])
    if(len(text)-1 > index):
        code.append("/")
    index +=1
print(" ".join([str(letter) for letter in code]))
