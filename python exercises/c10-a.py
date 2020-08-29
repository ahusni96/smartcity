import json

file = open("file.txt", "r")
outfile = open("output.txt", "w")

lines = 0
longList = []
globalList = []
dictionary = {}

for line in file:
    temp = str(line).rstrip(".\n")
    temp = temp.lower()
    words = temp.split(" ")

    globalList += words
    globalList.sort()

    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word

        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1 
    
    longList.append(longest.lower())
    lines += 1

longList.sort()

for item in longList:
    outfile.write(str(item) + "\n")

file.close()
outfile.close()

jsonDict = json.dumps(dictionary)

jsonFile = open("jsonFile.json", "w")
jsonFile.write(jsonDict)

print("Done writing to file")
jsonFile.close()
