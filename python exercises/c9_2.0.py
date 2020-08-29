# Define function called checkAnagram()
def checkAnagram(w1, w2):

	# Rearrange letters in ascending order
	w1 = sorted(w1)
	w2 = sorted(w2)

	# Output string
	print(w1)
	print(w2)

	# Check if the two words are anagram or not based on their list
	if w1 == w2:

		# Return true when both words have the same list
		return True
	else:

		# Return false when both have different lists
		return False

# ===== End function checkAnagram() =====

# Input strings
s1 = input("String 1: ")
s2 = input("String 2: ")

# Call checkAnagram function and pass the two inputs
bRes = checkAnagram(s1, s2)

# Check if the function returns True or False
if bRes == True:

	# Success
	print("The two words are anagrams")
else:

	# Failed
	print("The two words are not anagrams")