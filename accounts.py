# accounts.py
# Read in a 10 character account number and output the account number.
# From reading online I had to import re so I had the necessary capability to run this script.
# Once a 10 digit number is entered (also works if you enter a longer/shorter number), only the last 4 digits of the number
# are displayed.  The other numbers are masked with "X"s.

# Author: Nichola Walsh


import re

input = input("Please enter a 10 digit account number: ")

mask_first_4_numbers = 4
maskchar = "X"

input_total = sum(map(str.isdigit, input))
mask_last_4_numbers = input_total - mask_first_4_numbers
output = re.sub('\d', maskchar, input, mask_last_4_numbers)

print(output)