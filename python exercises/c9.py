def checkanagram(word1, word2):
	list1 = []
	list2 = []

	#==============================================
	# First Word (word1)
	#==============================================

	for alpha in word1:
		list1 += alpha
	
	list1 = sorted(list1)

	#==============================================
	# Second Word (word2)
	#==============================================

	for beta in word2:
		list2 += beta

	list2 = sorted(list2)

	if list1 == list2:
		return True
	else:
		return False

#============ End of function ============#

s1 = "stone"
s2 = "notee"

isAnagram = checkanagram(s1, s2)

if isAnagram is True:
	print("The two words are anagrams")
else:
	print("The two words are not anagrams")
