# take input from the user for the upper limit
num = int(input("Enter a number (greater than 1): "))

# loop through the range from 2 to num (inclusive)
for i in range(2, num + 1):
    # calculate the decimal equivalent of 1 divided by i
    decimal_value = 1 / i
    # print the result
    print(f"1/{i} = {decimal_value}")
