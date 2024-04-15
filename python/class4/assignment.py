PI =3.4

# Function to create a multiplication table for the given number
def multiplication_table(number):
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")

# Function to calculate GST and total price for items in McDonald's
def calculate_price(items):
    total_price = 0
    print("ITEM\t\tPrice\t\tGST")
    print("--------------------------------------")
    for item, price in items.items():
        gst = price * 18 / 100
        total_price += price + gst
        print(item,price,gst,sep="\t\t")
    print("--------------------------------------")
    print("Total price to be paid:",total_price)

# Functions to calculate perimeter of shapes
def circle_perimeter(radius):
    return 2 * PI * radius

def square_perimeter(side):
    return 4 * side

def triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3

print("="*100)
# Example usage
number = int(input("Enter a number to create its multiplication table: "))
multiplication_table(number)

print("="*100)

items = {
    "Fries": 50,
    "Burger": 70,
    "Coke": 25,
    "Pizza": 85
}
calculate_price(items)
print("="*100)

radius = float(input("Enter the radius of the circle: "))
print("Perimeter of the circle:", circle_perimeter(radius))
print("="*100)

side = float(input("Enter the side length of the square: "))
print("Perimeter of the square:", square_perimeter(side))
print("="*100)

side1 = float(input("Enter the first side length of the triangle: "))
side2 = float(input("Enter the second side length of the triangle: "))
side3 = float(input("Enter the third side length of the triangle: "))
print("Perimeter of the triangle:", triangle_perimeter(side1, side2, side3))
print("="*100)
