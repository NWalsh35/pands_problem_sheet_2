# collatz_sandbox.py
# Ask the user to input any positive integer.
# If the positive integer is an even number, divide the integer by 2. 
# If the postive integer is an odd number, multiply it by 3 and add 1.
# Have the program end at value one.
# If the current value is one, end the program. 
# One of the sources I found had an extra part to their code where they put it an error message that
# appears if the user inputs a number less than zero. I did not include this in this iteration as
# as it was not needed but is still useful. It is in the longer version of this code "collatz_longer.py" 
# for my own reference for future assignments. 


# Author: Nichola Walsh


number = int(input("Enter a positive integer: "))
  
my_seq = [number]
while number > 1:
    if number%2 == 0:
        number = number//2

        my_seq.append(number)
    else:
        number = (number*3)+1
        my_seq.append(number)
print(*my_seq)    