# Advent of Code 2015 - Day 4 - Problem 1

import hashlib

count = 1
while True:
	string = 'bgvyzdsv' + str(count)
	if hashlib.md5(string.encode('utf-8')).hexdigest()[:5] == "00000":
		break;
	count += 1
print(count)

# Advent of Code 2015 - Day 4 - Problem 2

import hashlib

count = 1
while True:
	string = 'bgvyzdsv' + str(count)
	if hashlib.md5(string.encode('utf-8')).hexdigest()[:6] == "000000":
		break;
	count += 1
print(count)
