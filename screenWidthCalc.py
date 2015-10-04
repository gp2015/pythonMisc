def screenWidth(screenWidthInPx):
	print screenWidthInPx
	iphone5 = 480.0/568.0
	print iphone5
	mediaWidth = iphone5 * float(screenWidthInPx)
	print mediaWidth
	return round(mediaWidth)
	
print screenWidth(raw_input("Enter the screen width to receive the img width property: "))