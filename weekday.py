#Firstly, we need to import the datetime module
import datetime

# Get todays date and time using the:
now = datetime.datetime.now()

# Get the weekday- ( "weekday()"" gives a number for each day of the week - 0 = Monday, 1 = Tuesday, 2 = Wednesday...)
weekday = now.weekday()

# Check if today is a weekday or a weekend 0-4 are weekdays, 5 & 6 are not using if and else functions
if weekday < 5:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It's the weekend, yay!")