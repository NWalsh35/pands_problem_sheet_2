# Bank.py
# Week 2 problem sheet: program to add two numbers and convert cents to euro. 
# Author: Nichola Walsh




number1 = int(input('Please enter first amount in cents:'))
number2 = int(input('Please enter second amount in cents:'))
newnumber = number1 + number2
total = newnumber/100

print (f'The sum is: €{total}')