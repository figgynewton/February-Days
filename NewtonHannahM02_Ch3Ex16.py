Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> year = int(input(" Enter a year: "))
 Enter a year: 2000
>>> if (year % 4) == 0:
	if (year % 100) == 0:
		if (year % 400) == 0:
			print("{0} is not a leap year". format(year))
		else:
			print("{0} is not a leap year". format(year))
	else:
		print("{0} is a leap year"> format(year))
else:
	print("{0} is not a leap year". format(year))

	
2000 is not a leap year
>>> 