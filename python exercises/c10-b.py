import json

jsonFile = open("jsonFile.json", "r")

dictionary = json.loads(jsonFile.read())

print(dictionary)

for wrd in sorted(dictionary, key = dictionary.get, reverse = True):
    print("{} ({})".format(wrd, dictionary[wrd]))
