# Function to calculate the sum of even Fibonacci numbers
def sum_even_fibonacci(limit):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    even_sum = 0

    # Loop to generate Fibonacci numbers and sum the even ones
    while b <= limit:
        if b % 2 == 0:
            even_sum += b
        # Update the Fibonacci numbers
        a, b = b, a + b

    return even_sum

# Take input from the user for the upper limit
limit = int(input("Enter the limit for the Fibonacci sequence: "))

# Get the sum of even Fibonacci numbers that do not exceed the limit
result = sum_even_fibonacci(limit)

# Print the result
print(f"The sum of the even Fibonacci numbers whose values do not exceed {limit} is: {result}")
