# Taking input from the user for a list
n = int(input("Enter the number of elements in the list: "))
list_elements = []  # initialize an empty list

# Getting list elements from the user
for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    list_elements.append(element)  # append each element to the list

# Display the list
print("The list you entered is:", list_elements)

# Converting the list into a tuple
tuple_elements = tuple(list_elements)

# Display the tuple
print("The tuple equivalent is:", tuple_elements)
