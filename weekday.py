# Week 5 task
# Aim: write a program that outputs whether or not today is a weekday.
# If the day of the week is a weekday, the program should output "Yes, unfortunately today is a weekday".
# If the day of the week is at the weekend, the program should output "It is the weekend, yay!"

# Reasoning:  Python converts each day of the week into an integer. Monday = 0, Tuesday = 1,
# Wednesday = 2, Thursday = 3, Friday = 4, Saturday = 5, Sunday = 6.
# Specified that x = the integer day of the week.
# If x is less than or equal to 4, i.e. Monday to Friday, then print "Yes, unfortunately today is a
# weekday"
# Else, x is 5 or 6 which means Saturday or Sunday, then print "It is the weekend, yay!"
# Used website "https://pynative.com/python-get-the-day-of-week/#:~:text=Use%20the%20weekday()%20method,%2C%2002)%20is%20a%20Monday."
# to get the day of the week as an integer but then I worked out the last part myself.

# Author: Nichola Walsh


from datetime import datetime

#get current date time
dt = datetime.now()

# print the day of the week as an integer value 0 - 6
x = dt.weekday()

if x <= 4:
    print("Yes, unfortunately today is a weekday")

else:
    print("It is the weekend, yay!")
