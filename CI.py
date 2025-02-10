# Function to calculate Simple Interest
def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Function to calculate Compound Interest
def calculate_compound_interest(principal, rate, time):
    compound_interest = principal * (1 + rate / 100) ** time - principal
    return compound_interest

# Take input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time period (in years): "))

# Calculate Simple Interest and Compound Interest
simple_interest = calculate_simple_interest(principal, rate, time)
compound_interest = calculate_compound_interest(principal, rate, time)

# Print the results
print(f"\nSimple Interest is: {simple_interest}")
print(f"Compound Interest is: {compound_interest}")
