# Advent of Code 2015 - Day 2 - Problem 1

file = open('adventofcode2015-2-input.txt', 'r')
Lines = file.readlines() #lxwxh

total = 0
rTotal = 0
for line in Lines:
	dimensions = line.split("x")
	l = int(dimensions[0])
	w = int(dimensions[1])
	h = int(dimensions[2])
	total = total + 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
	rTotal = rTotal + min(2*l+2*w, 2*w+2*h, 2*h+2*l) + l*w*h

print(total)
print(rTotal)


