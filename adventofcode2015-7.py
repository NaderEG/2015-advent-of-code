# Advent of Code 2015 - Day 7 - Problem 1

file = open('adventofcode2015-7-input.txt', 'r')
Lines = file.readlines()

wires = {}

for line in Lines:
	wires[line.split()[-1]] = line.split()[:-2]

