# Taking input from the user to create a sequence
n = int(input("Enter the number of elements: "))

# Creating a list by taking user inputs
user_input_list = []
for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    user_input_list.append(element)

# Loop over the sequence (list) and print each element
print("\nThe elements in the list are:")
for element in user_input_list:
    print(element)
