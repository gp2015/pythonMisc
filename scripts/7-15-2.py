def reverse(text):
    i = -1
    reversedText = ""
    for letter in text:
        reversedText += text[i]
        i -= 1
    return reversedText
    
    
print reverse('fart')