import math

def calculate_circle_area(radius):
    # The formula for the area of a circle is A = π * r^2
    area = math.pi * radius**2
    return area

# Example usage:
radius = float(input("Enter the radius of the circle: "))
area_result = calculate_circle_area(radius)

print(f"The area of the circle with radius {radius} is: {area_result:.2f}")