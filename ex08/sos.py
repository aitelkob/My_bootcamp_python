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




"""""if len(sys.argv) < 2:
		print("ERROR")
		return
	for each in sys.argv[1:]:
		if not each.replace(' ','').isalnum():
			print("ERROR")
			return
	for each in sys.argv[1:]:
		for c in each:
			if c == ' ':
				print(" / ", end='')
			else:
				print(chars[c.upper()], end='')
		if each != sys.argv[-1]:
			print(" / ", end='')
		else:
			print()"""""
if len(sys.argv) <= 1:
    exit()


code = []
text = [string.upper() for string in sys.argv[1:]]
for string in args:
    res.append(" ".join([morse_dict[letter] for letter in string]))

print(code)
