# Advent of Code 2015 - Day 6 - Problem 1

def turnOn(arr, sx, sy, ex, ey):
	for i in range(sx, ex):
		for j in range(sy, ey):
			arr[i][j] = True

def turnOff(arr, sx, sy, ex, ey):
	for i in range(sx, ex):
		for j in range(sy, ey):
			arr[i][j] = False

def toggle(arr, sx, sy, ex, ey):
	for i in range(sx, ex):
		for j in range(sy, ey):
			arr[i][j] = not arr[i][j]


rows = 1000
cols = 1000
lights = [[False] * rows for i in range(cols)]

file = open('adventofcode2015-6-input.txt', 'r')
Lines = file.readlines()

for line in Lines:
	x = line.split()
	if x[0] == "toggle":
		sx, sy = x[1].split(",")
		ex, ey = x[3].split(",")
		toggle(lights, int(sx), int(sy), int(ex)+1, int(ey)+1)
	elif x[1] == "on":
		sx, sy = x[2].split(",")
		ex, ey = x[4].split(",")
		turnOn(lights, int(sx), int(sy), int(ex)+1, int(ey)+1)
	elif x[1] == "off":
		sx, sy = x[2].split(",")
		ex, ey = x[4].split(",")
		turnOff(lights, int(sx), int(sy), int(ex)+1, int(ey)+1)

count = 0
for i in range(1000):
	for j in range(1000):
		if lights[i][j] == True:
			count += 1
print(count)

# Advent of Code 2015 - Day 6 - Problem 2

def turnOn2(arr, sx, sy, ex, ey):
	for i in range(sx, ex):
		for j in range(sy, ey):
			arr[i][j] = arr[i][j] +1

def turnOff2(arr, sx, sy, ex, ey):
	for i in range(sx, ex):
		for j in range(sy, ey):
			if arr[i][j] > 0:
				arr[i][j] = arr[i][j] -1 

def toggle2(arr, sx, sy, ex, ey):
	for i in range(sx, ex):
		for j in range(sy, ey):
			arr[i][j] = arr[i][j] +2


rows = 1000
cols = 1000
lights = [[0] * rows for i in range(cols)]

file = open('adventofcode2015-6-input.txt', 'r')
Lines = file.readlines()

for line in Lines:
	x = line.split()
	if x[0] == "toggle":
		sx, sy = x[1].split(",")
		ex, ey = x[3].split(",")
		toggle2(lights, int(sx), int(sy), int(ex)+1, int(ey)+1)
	elif x[1] == "on":
		sx, sy = x[2].split(",")
		ex, ey = x[4].split(",")
		turnOn2(lights, int(sx), int(sy), int(ex)+1, int(ey)+1)
	elif x[1] == "off":
		sx, sy = x[2].split(",")
		ex, ey = x[4].split(",")
		turnOff2(lights, int(sx), int(sy), int(ex)+1, int(ey)+1)

count = 0
for i in range(1000):
	for j in range(1000):
		count = count + lights[i][j]
print(count)