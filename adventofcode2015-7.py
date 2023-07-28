# Advent of Code 2015 - Day 7 - Problem 1

file = open('adventofcode2015-7-input.txt', 'r')
Lines = file.readlines()

wires = {}
signals = {}

for line in Lines:
	wires[line.split()[-1]] = line.split()[:-2]

for wire in wires:
	recurse(wire)

recurse(wire):
	if(len(wires[wire]) == 1):
		signals[wire] = int(wires[wire][0])
	elif(len(wires[wire]) == 2 and isnumeric(wires[wire])):
		signals[wire] = ~int(wires[wire][1])
	elif(len(wires[wire]) == 2 and not isnumeric(wires[wire])):
		signals[wire] == ~int(recurse(wires[wire][1]))
	elif(len(wires[wire]) == 3 and isnumeric(wires[wire][0]) and isnumeric(wires[wire][2])):
		
		


