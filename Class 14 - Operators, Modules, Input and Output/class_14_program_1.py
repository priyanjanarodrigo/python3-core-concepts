# Prints the area of a circle with the given radius

from math import pi

radius = float(input("Enter the radius of the circle: "))
area = pi * (radius ** 2)

# {area:.2f} means that the area should be printed with 2 decimal places.
print(f"The area of the circle with radius {radius} is {area:.2f} square units.")
