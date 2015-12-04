def censor(text, word):
	print "\n"
	print "text: " + text
	print "word: " + word
	censorship = len(word) * "*"
	print "censorship: " + censorship
	senSplit = text.split()
	print "senSplit: "
	print senSplit
	i = 0
	print "i: "
	print i
	for i in range(0, len(senSplit)):
		if word == senSplit[i]:
			print "Word in if: " + word
			print "senSplit in if: " + senSplit[i]
			senSplit[i] = censorship
			print "senSplit[i] in if: " + senSplit[i]
			i += 1
			print "i in if: "
			print i
	senJoin = " ".join(senSplit)
	print "senJoin: " + senJoin
	return senJoin
	
	
print censor('fuck asshole fuck', 'fuck')
print censor('hey hey hey', 'hey')


def censor(text, word):
	censorship = len(word) * "*"
	senSplit = text.split()
	i = 0
	if senSplit[i] == word:
		senSplit[i] = censorship
		i += 1
	senJoin = " ".join(senSplit)
	return senJoin
	
	
print censor('hey hey hey', 'hey')	