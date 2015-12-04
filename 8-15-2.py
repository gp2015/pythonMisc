def anti_vowel(text):
	vowels = "aeiouAEIOU"
	newText = None
	newText = str(newText)
	for letter in text not in vowels:
		letter = str(letter)
			newText += letter
	return newText
		
	
print anti_vowel("fArting")

def anti_vowel(text):
	vowels = "aeiouAEIOU"
	noVowels = ""
	for letter in text:
		if letter not in vowels:
			noVowels += letter
	return noVowels
	

#frtng
print anti_vowel("fartING")