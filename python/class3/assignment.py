#grade system
score = int(input("Enter your score: "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Your grade is:", grade)
print("\n\n==================================================================\n\n")

#time of the day
hour = int(input("Enter the hour (in 24-hour format): "))

if hour < 12:
    time_of_day = 'morning'
elif hour < 18:
    time_of_day = 'afternoon'
elif hour < 22:
    time_of_day = 'evening'
else:
    time_of_day = 'night'

print("It's", time_of_day)

print("\n\n==================================================================\n\n")
fruits = ['apple', 'banana', 'orange', 'grape']

for fruit in fruits:
    print(fruit, end=" ")
print()

colors = ['red', 'blue', 'green', 'yellow']

for color in colors:
    print(color, end=" ")
print()

print("\n\n==================================================================\n\n")

for i in range(10, 0, -1):
    print(i, end=" ")
print()

for i in range(1, 11):
    print(i, end=" ")
print()

print("\n\n==================================================================\n\n")
# Mobile Phone prices according to brand
brands = ["Samsung", "Apple", "Google", "OnePlus"]

print("Available Brands:", brands)
brand_prices = {
    "Samsung": 8000,
    "Apple": 100000,
    "Google": 90000,
    "OnePlus": 22000
}

user_brand = input("Choose a brand: ")

if user_brand in brand_prices:
    print("You have selected", user_brand, "and its price is", brand_prices[user_brand], "INR")
else:
    print("Sorry, we don't have that brand available.")

print("\n\n==================================================================\n\n")
