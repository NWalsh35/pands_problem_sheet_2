# collatz.py
# Ask the user to input any positive integer.
# If the positive integer is an even number, divide the integer by 2. 
# If the postive integer is an odd number, multiply it by 3 and add 1.
# Have the program end at 2.
# If the current value is one, end the program. 

# Author: Nichola Walsh

while True:
    try:
        number = int(input("Enter a positive integer: "))
        if number < 0:
            raise ValueError
        break
    except ValueError:

        print("That is not a positive integer.  Please try again.")

my_seq = [number]
while number > 1:
    if number%2 == 0:
        number = number//2

        my_seq.append(number)
    else:
        number = (number*3)+1
        my_seq.append(number)
print(*my_seq, sep = ", ")        



