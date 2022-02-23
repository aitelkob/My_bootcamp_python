languages = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

[print("{} was created by {}".format(key,value)) for key,value in languages.items()]
