def anti_vowel(text):
    vowels = "aeiouAEIOU"
	newText = None
    for letter in text:
        if letter in text not in vowels:
            newText += letter
	return newText
			
		
print anti_vowel('farting')