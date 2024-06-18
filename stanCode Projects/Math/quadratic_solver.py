"""
File: quadratic_solver.py
Name: Zoe
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	I have to solve the quadratic equation by characterizing its discriminant.
	If discriminant > 0, print 2 roots
	If discriminant = 0, print 1 root
	If discriminant < 0, print "No real roots"
	"""
	print('stanCode Quadratic Solver!')
	a = float(input('Enter a = '))
	b = float(input('Enter b = '))
	c = float(input('Enter c = '))
	dis = b*b - 4*a*c

	if a != 0:
		if dis > 0:
			print('Two roots: ' + str((-b + math.sqrt(dis)) / (2*a)) + ' , ' + str((-b - math.sqrt(dis)) / (2*a)))
		elif dis == 0:
			print('One root: ' + str(-b / (2 * a)))
		else:
			print('No real roots')
	else:
		print('a cannot be 0!')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
