import json

file = open("allwords.json", "r")

string = file.read()

dictionary = json.loads(string)

print(dictionary)

# Loop each word in dictionary
for word in sorted(dictionary, key = dictionary.get, reverse = True):
	
	# Output each item in dictionary
	print("{}, {}".format(word, dictionary[word]))