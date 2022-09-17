# Advent of Code 2015 - Day 5 - Problem 1

def containsThreeVowels(string):
	vowels = ["a", "e", "i", "o", "u"]
	count = 0
	for char in string:
		if char in vowels:
			count += 1
	return count >= 3

def twoInARow(string):
	for pos in range(len(string)-1):
		if string[pos] == string[pos+1]:
			return True
	return False

def dncSubstring(string):
	matches = ["ab", "cd", "pq", "xy"]
	return not any(x in string for x in matches)

file = open('adventofcode2015-5-input.txt', 'r')
Lines = file.readlines()
nicestrings = 0

for line in Lines:
	if containsThreeVowels(line) and twoInARow(line) and dncSubstring(line):
		nicestrings += 1
print(nicestrings)

# Advent of Code 2015 - Day 5 - Problem 2

def twoPairs(string):
	for i in range(len(string)-1):
		for j in range(i+2, len(string)-1):
			if string[i] + string[i+1] == string[j] + string[j+1]:
				return True
	return False

def repeatsWithLetterBetween(string):
	for i in range(len(string)-2):
		if string[i] == string[i+2]:
			return True
	return False

file = open('adventofcode2015-5-input.txt', 'r')
Lines = file.readlines()
nicestrings = 0

for line in Lines:
	if repeatsWithLetterBetween(line) and twoPairs(line):
		nicestrings += 1
print(nicestrings)