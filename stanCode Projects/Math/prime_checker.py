"""
File: prime_checker.py
Name: Zoe
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
	"""
	Ask user to enter an integer(n)
	Characterize whether n is a prime number.
	If n is a prime number, print " (n) is a prime number"
	Otherwise print " (n) is not a prime number"
	"""
	print('Welcome to the prime checker!')
	n = int(input('n: '))
	while n != EXIT:
		if is_prime(n):									# check whether n is a prime number
			print(str(n) + ' is a prime number')
		else:
			print(str(n) + ' is not a prime number')
		n = int(input('n: '))
	print('Have a good one!')


def is_prime(n):
	"""
	Check whether n is prime
	If true, n is a prime number
	If false, n is not a prime number
	"""
	if n == 2:					# 2 is a prime number (even)
		return True
	for i in range(2, n):		# 2 ~ (n-1)
		if n % i == 0:			# if n is divisible, n is not a prime number
			return False
	return True					# Otherwise, n is a prime number


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
