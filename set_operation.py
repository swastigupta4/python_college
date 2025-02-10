# Take input from the user to create a set
n = int(input("Enter the number of elements in the set: "))
user_set = set()

# Taking user input for the set elements
for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    user_set.add(element)  # Add the element to the set

# Display the original set
print("\nThe original set is:", user_set)

# Take another set input from the user for operations
m = int(input("\nEnter the number of elements for another set: "))
other_set = set()

for i in range(m):
    element = input(f"Enter element {i + 1}: ")
    other_set.add(element)

# Display the second set
print("\nThe second set is:", other_set)

# Perform set operations

# Union of two sets
union_result = user_set.union(other_set)
print("\nUnion of the sets:", union_result)

# Intersection of two sets
intersection_result = user_set.intersection(other_set)
print("\nIntersection of the sets:", intersection_result)

# Difference of two sets
difference_result = user_set.difference(other_set)
print("\nDifference of the first set from the second set:", difference_result)

# Symmetric Difference of two sets
symmetric_difference_result = user_set.symmetric_difference(other_set)
print("\nSymmetric Difference of the sets:", symmetric_difference_result)

# Check if the first set is a subset of the second set
is_subset = user_set.issubset(other_set)
print("\nIs the first set a subset of the second set?", is_subset)

# Check if the first set is a superset of the second set
is_superset = user_set.issuperset(other_set)
print("\nIs the first set a superset of the second set?", is_superset)

# Check if the two sets are disjoint
are_disjoint = user_set.isdisjoint(other_set)
print("\nAre the two sets disjoint?", are_disjoint)
