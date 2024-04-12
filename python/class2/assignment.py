# 1. Create a list and provide at least 2 examples of following actions:
print("\n\n========================LIST===============================\n\n")

#  - append
tld_list = ["com", "org", "app", "edu", "gov", "uk", "blog", "app"]
print("Before append 3 elements:", tld_list)
tld_list.append("mil")
tld_list.append("info")
tld_list.append("biz")
print("After append 3 elements:", tld_list)
print("________________________________________")

#  - insert
print("Before insert elements:", tld_list)
tld_list.insert(0, "io")
tld_list.insert(1, "co")
print("After insert elements:", tld_list)
print("________________________________________")

#  - remove
print("Before remove elements:", tld_list)
tld_list.remove("uk")
tld_list.remove("blog")
print("After remove elements:", tld_list)
print("________________________________________")

#  - pop
print("Before pop elements:", tld_list)
tld_list.pop(-6)
tld_list.pop(1)
print("After pop elements:", tld_list)
print("________________________________________")

#  - index
print("Before index elements:", tld_list)
print("Index of the element 'app' is ", tld_list.index("app"))
print("Index of the element 'gov' is ", tld_list.index("gov"))
print("________________________________________")

#  - count
print("Before count elements:", tld_list)
print("Count of the element 'app' is ", tld_list.count("app"))
print("Count of the element 'gov' is ", tld_list.count("gov"))
print("________________________________________")

print("\n\n========================TUPLE===============================\n\n")
# 2. Create a tuple and provide at least 2 examples of following actions:
tld_tuple = ("com", "org", "app", "edu", "gov", "uk", "blog", "app", "de")

#  - index
print("Before index elements:", tld_tuple)
print("Index of 'com' in tuple is ", tld_tuple.index("com"))
print("Index of 'org' in tuple is ", tld_tuple.index("org"))
print("________________________________________")

#  - count
print("Before Count elements:", tld_tuple)
print("Count of 'edu' in tuple is ", tld_tuple.count("edu"))
print("Count of 'blog' in tuple is ", tld_tuple.count("blog"))
print("________________________________________")


# 3. Create a dictionary and provide at least 2 examples of following actions:
print("\n\n========================DICTIONARY===============================\n\n")
element_metadata={
   "name":"string_element",
   "address":"inside_list",
   "index":2,
   "value":"Naman"
}

file_metadata = {
    'name': 'example.txt',
    'size': 1024,
    'type': 'text'
}

print("element_metadata:",element_metadata)
print("file_metadata:",file_metadata)
print()

#  - keys
print("Keys from dict element_metadata:", element_metadata.keys())
print("Keys from dict file_metadata:", file_metadata.keys())
print("________________________________________")
#  - values

print("Values from dict element_metadata:", element_metadata.values())
print("Values from dict file_metadata:", file_metadata.values())
print("________________________________________")
#  - get

print("Get value for the key 'index' in element_metadata:", element_metadata.get("index"))
print("Get value for the key 'address' in element_metadata:", element_metadata.get("address"))

print("Get value for the key 'name' in file_metadata:", file_metadata.get("name"))
print("Get value for the key 'type' in file_metadata:", file_metadata.get("type"))

# 4. As list, tuple, and dictionary are collections of objects and objects
print("\n\n========================NESTED STRUCTURE===============================\n\n")

# List inside list - Example 1: Student records
students_math = ['Amit', 'Manish', 'Rahul']
students_science = ['Jeet', 'Sunil', 'Pravin']
students_history = ['Vishal', 'Karma', 'Jainil']
students_inside_list = [students_math, students_science, students_history]

# List inside list - Example 2: Employee details
hr_department = ['Amit', 'Jeet', 'Sunil']
it_department = ['Manish', 'Rahul', 'Pravin']
finance_department = ['Vishal', 'Karma', 'Jainil']
departments_inside_list = [hr_department, it_department, finance_department]

# Tuple inside list - Example 1: Coordinates of cities
city_coordinates = [(40.7128, -74.0060), (34.0522, -118.2437), (51.5074, -0.1278)]

# Tuple inside list - Example 2: Dates of events
event_dates = [('2022-05-20', 'Ghatkopar'), ('2022-06-15', 'Dadar'), ('2022-07-10', 'Andheri'), ('2022-07-10', 'Juhu')]

# Dictionary inside list - Example 1: Product details
product1 = {'name': 'Laptop', 'price': 999, 'brand': 'Dell'}
product2 = {'name': 'Smartphone', 'price': 499, 'brand': 'Samsung'}
products_inside_list = [product1, product2]

# Dictionary inside list - Example 2: Customer details
customer1 = {'name': 'Amit', 'age': 30, 'email': 'Amit@example.com'}
customer2 = {'name': 'Manish', 'age': 25, 'email': 'Manish@example.com'}
customers_inside_list = [customer1, customer2]

# List inside tuple - Example 1: Coordinates of cities
city_coordinates_tuple = ((40.7128, -74.0060), (34.0522, -118.2437), (51.5074, -0.1278))

# List inside tuple - Example 2: Temperature readings
temperature_readings = ([25, 30, 27], [18, 20, 19])

# Tuple inside tuple - Example 1: Coordinates of locations
location_coordinates = ((40.7128, -74.0060), (34.0522, -118.2437), (51.5074, -0.1278))

# Tuple inside tuple - Example 2: Dates and times
event_datetime = (('2022-05-20', '10:00'), ('2022-06-15', '09:30'), ('2022-07-10', '14:00'))

# Dictionary inside tuple - Example 1: Product details
product1_tuple = {'name': 'Laptop', 'price': 999, 'brand': 'Dell'}
product2_tuple = {'name': 'Smartphone', 'price': 499, 'brand': 'Samsung'}
products_inside_tuple = (product1_tuple, product2_tuple)

# Dictionary inside tuple - Example 2: Customer details
customer1_tuple = {'name': 'Amit', 'age': 30, 'email': 'Amit@example.com'}
customer2_tuple = {'name': 'Manish', 'age': 25, 'email': 'Manish@example.com'}
customers_inside_tuple = (customer1_tuple, customer2_tuple)

# List inside dictionary - Example 1: Product categories
product_categories = {'electronics': ['Laptop', 'Smartphone', 'Tablet'], 'clothing': ['T-shirt', 'Jeans', 'Dress']}

# List inside dictionary - Example 2: Employee departments
employee_departments = {'IT': ['Manish', 'Rahul', 'Pravin'], 'HR': ['Amit', 'Jeet', 'Sunil']}

# Tuple inside dictionary - Example 1: Product details
product1_dict = {'name': 'Laptop', 'price': 999, 'brand': 'Dell'}
product2_dict = {'name': 'Smartphone', 'price': 499, 'brand': 'Samsung'}
products_inside_dict = {'product1': product1_dict, 'product2': product2_dict}

# Tuple inside dictionary - Example 2: Customer details
customer1_dict = {'name': 'Amit', 'age': 30, 'email': 'amit@example.com'}
customer2_dict = {'name': 'Manish', 'age': 25, 'email': 'manish@example.com'}
customers_inside_dict = {'customer1': customer1_dict, 'customer2': customer2_dict}

# Dictionary inside dictionary - Example 1: User profiles
user1_profile = {'name': 'Amit', 'age': 30, 'email': 'amit@example.com'}
user2_profile = {'name': 'Manish', 'age': 25, 'email': 'manish@example.com'}
users_inside_dict = {'user1': user1_profile, 'user2': user2_profile}

# Dictionary inside dictionary - Example 2: Product inventory
product1_inventory = {'quantity': 100, 'price': 999}
product2_inventory = {'quantity': 200, 'price': 499}
products_inside_dict2 = {'product1': product1_inventory, 'product2': product2_inventory}

# Nested Structures Examples
print("List inside list 1 (Student records):", students_inside_list)
print()
print("List inside list 2 (Employee details):", departments_inside_list)
print()
print("Tuple inside list 1 (Coordinates of cities):", city_coordinates)
print()
print("Tuple inside list 2 (Dates of events):", event_dates)
print()
print("Dictionary inside list 1 (Product details):", products_inside_list)
print()
print("Dictionary inside list 2 (Customer details):", customers_inside_list)
print()
print("List inside tuple 1 (Coordinates of cities):", city_coordinates_tuple)
print()
print("List inside tuple 2 (Temperature readings):", temperature_readings)
print()
print("Tuple inside tuple 1 (Coordinates of locations):", location_coordinates)
print()
print("Tuple inside tuple 2 (Dates and times):", event_datetime)
print()
print("Dictionary inside tuple 1 (Product details):", products_inside_tuple)
print()
print("Dictionary inside tuple 2 (Customer details):", customers_inside_tuple)
print()
print("List inside dictionary 1 (Product categories):", product_categories)
print()
print("List inside dictionary 2 (Employee departments):", employee_departments)
print()
print("Tuple inside dictionary 1 (Product details):", products_inside_dict)
print()
print("Tuple inside dictionary 2 (Customer details):", customers_inside_dict)
print()
print("Dictionary inside dictionary 1 (User profiles):", users_inside_dict)
print()
print("Dictionary inside dictionary 2 (Product inventory):", products_inside_dict2)
