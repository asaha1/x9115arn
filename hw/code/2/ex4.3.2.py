from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = 0

def square(t, length):
	for i in range(4):
		fd(t, length)
		lt(t)

def polygon(t, length, n, angle):
	for i in range(angle):
		fd(t, length)
		lt(bob, 360 / n)

# square(bob, 100)

'''Number 1
'''
for i in range(6):
	polygon(bob, 1, 360, 60)
	lt(bob, 120)
	polygon(bob, 1, 360, 60)
	lt(bob, 180)

pu(bob)
fd(bob, 150)
pd(bob)
'''Number 2
'''

for i in range(12):
	polygon(bob, 1, 360, 60)
	lt(bob, 120)
	polygon(bob, 1, 360, 60)
	lt(bob, 150)

pu(bob)
fd(bob, 150)
pd(bob)

'''Number 3
'''

for i in range(12):
	polygon(bob, 2, 360, 30)
	lt(bob, 150)
	polygon(bob, 2, 360, 30)
	lt(bob, 180)

def triangle(t, radius, sides):
	angle = 90.0 + 180.0 / sides
	sideLength = 2 * radius * math.sin(math.radians(180 / sides))
	print angle
	for i in range(sides):
		fd(t, radius)
		lt(t, angle)
		fd(t, sideLength)
		lt(t, angle)
		fd(t, radius)
		lt(t, 180)
'''
triangle(bob, 50, 5)
pu(bob)
fd(bob, 150)
pd(bob)
triangle(bob, 50, 6)
pu(bob)
fd(bob, 150)
pd(bob)
triangle(bob, 50, 7)'''
wait_for_user()