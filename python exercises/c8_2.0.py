# Open file in read mode
fileIn = open("file3.txt", "r")

# List of longest words
longestList = []

# Declare empty dictionary
dictionary = {}

# Loop to read each line in a file
for line in fileIn:
	
	# Remove "\n" from word
	line = line.rstrip("\n")

	# Separate into words (list)
	words = line.split(" ")

	# Count words in line
	count = 0

	# Store longest word (string)
	longest = ""

	# Loop to count words
	for word in words:

		# Remove "."
		word = word.rstrip(".")
		
		# Change to lowercase
		word = word.lower()

		# Check if word is in dictionary
		if word not in dictionary:
			
			# Add word to dictionary
			dictionary[word] = 1

		# If word already in dictionary
		else:

			# Increment word count
			dictionary[word] += 1

		# Check if current word is longer than current longest
		if len(word) > len(longest):
			
			# Set longest to current word
			longest = word

		# Increment word count
		count += 1

	# print("{} - {} words".format(line, count))
	# print(longest)

	# Add longest word into list
	longestList.append(longest)

# Sort longestList
longestList.sort()

# Open file for output
fileOut = open("output2.txt", "w")

# Loop to write one word per line
for word in longestList:
	
	# Writing to file
	fileOut.write(word + "\n")

# Close file after using it
fileIn.close()
fileOut.close()

# Writing dictionary to CSV file
csv = open("csv2.csv", "w")

# Loop each word in dictionary
for word in sorted(dictionary, key = dictionary.get, reverse = True):
	
	# Output each item in dictionary
	csv.write("{}, {}\n".format(word, dictionary[word]))

# Close csv
csv.close()
