# get user input
num = int(input("enter a number: "))  # take input and convert to integer

# check if the number is even
if num % 2 == 0:
    print("the number is even")  # if remainder when divided by 2 is 0, it's even
else:
    print("the number is odd")  # if remainder is not 0, it's odd
