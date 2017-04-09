def reverse(text):
	i = -1
	reversedText = []
	final = ""
	for letter in text:
		textLetter = text[i]
		i = i - 1
		reversedText.append(textLetter)
	for item in range(0, len(reversedText)):
		final += str(reversedText[item])
	return final
		

print reverse('Python!')

def reverse(text):
	i = -1
	reversedText = []
	final = ""
	for letter in text:
		textLetter = text[i]
		i -= 1
		reversedText.append(textLetter)
	for item in range(0, len(reversedText)):
		final += str(reversedText[item])
	return final
	
print reverse('hello')