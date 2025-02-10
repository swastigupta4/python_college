import math  # importing math module to use sqrt function

# taking input for the coordinates of the first point
x1 = float(input("Enter the x-coordinate of the first point: "))  
y1 = float(input("Enter the y-coordinate of the first point: "))  

# taking input for the coordinates of the second point
x2 = float(input("Enter the x-coordinate of the second point: "))  
y2 = float(input("Enter the y-coordinate of the second point: "))  

# applying the distance formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  

# displaying the computed distance
print(f"The distance between the two points is: {distance:.2f}")
