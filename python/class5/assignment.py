def calculate_rectangle_area(length: float, breadth: float) -> float:
    return length * breadth

def calculate_circle_area(radius: float) -> float:
    import math
    return math.pi * radius ** 2



import math

# Calculate the square root of a number
number = 25
square_root = math.sqrt(number)
print("Square root of", number, "is", square_root)


import os

def list_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            print(os.path.join(root, file))

# Example usage
directory_path = "../.."
list_files(directory_path)
