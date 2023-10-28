line = 32 * '_'
print(line)
import math

def calculate_circle_area(radius):
    return math.pi * radius**2

if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle: "))
    area = calculate_circle_area(radius)
    print(f"The area of the circle with radius {radius} is {area:.2f}")
