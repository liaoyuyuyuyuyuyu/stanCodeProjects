"""
File: weather_master.py
Name: Zoe
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

EXIT = -100


def main():
	"""
	Ask user to enter a integer(data).
	If data != EXIT, ask user to enter another data.
	If data = EXIT, show the highest, lowest, average temperature, and cold days.
	"""
	print('stanCode \"Weather Master 4.0\"!')
	data = int(input('Next temperature: (or ' + str(EXIT) + ' to quit)? '))
	times = 1				# Record how many times user enters a number
	cold_days = 0			# Record there are how many cold days

	if data == EXIT:
		print('No temperatures were entered.')
	else:
		# in case user only enters once
		maximum = data
		minimum = data
		total = data
		if data < 16:
			cold_days = cold_days + 1
		# when user enters data more than once
		while data != EXIT:
			data = int(input('Next temperature: (or ' + str(EXIT) + ' to quit)? '))
			if data != EXIT:
				total = data + total			# Record total to calculate Average
				times = times + 1				# Record how many times user enters a number
				if data > maximum:
					maximum = data
				if data < minimum:
					minimum = data
				if data < 16:					# Record there are how many cold days
					cold_days = cold_days + 1
		# after user enters "EXIT"
		avg = float(total) / times
		print('Highest temperature = ' + str(maximum))
		print('Lowest temperature = ' + str(minimum))
		print('Average = ' + str(avg))
		print(str(cold_days) + ' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
