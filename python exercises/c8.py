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

    #line = str(line).rstrip("\n")
    #print(line + " -" + str(len(words)) + " words")

    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word

        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1 
    
    #print(line + " - Longest word is " + longest)
    #print("Longest word is " + longest)
    longList.append(longest.lower())
    lines += 1

#print("There are " + str(lines) + " lines")
longList.sort()
#print(longList)

for item in longList:
    outfile.write(str(item) + "\n")

file.close()
outfile.close()

csv = open("allwords.csv", "w");

for wrd in sorted(dictionary, key = dictionary.get, reverse = True):
    csv.write("{}, {}\n".format(wrd, dictionary[wrd]))
