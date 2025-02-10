# Take input from the user for three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the largest number
largest = num1  # Assume num1 is the largest initially

if num2 > largest:
    largest = num2  # Update largest if num2 is greater
if num3 > largest:
    largest = num3  # Update largest if num3 is greater

# Print the largest number
print(f"The largest number is: {largest}")
