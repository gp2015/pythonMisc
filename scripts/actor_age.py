# pg 32

from __future__ import division

actor_age = [31, 32, 32, 33, 35, 36, 37, 37, 38, 38, 39, 40, 40, 40, 42, 42, 
43, 43, 45, 45, 46, 47, 48, 48, 51, 55, 55, 56, 60, 60, 61, 76]

def actor_age_mean():
	
	sum = 0
	
	for x in range(0, len(actor_age)):
		sum += actor_age[x]
	
	answer = 0
	answer = float(sum / len(actor_age))
	return answer

def actor_age_median(): # correct median algorithm

def q1q3: # Q1, Q3 algorithm

def IQR: # IQR algorithm

def 5num: # five-number summary algorithm
	
# Test cases

print "Answer a: %s" % (len(actor_age)) # 32

print "Answer b: %s" % (actor_age_mean()) # 44.72

# 31, 37.75, 42.5, 48.75, 76
print "Answer c: %s, %s, %s" % (min(actor_age), actor_age_median(), max(actor_age)) 