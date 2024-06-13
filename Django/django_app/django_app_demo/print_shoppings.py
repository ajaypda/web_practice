from shopping.models import Product, Review

def print_products():
    instances = Product.objects.all()
    print("=================================================================")
    for _ in instances:
        print("--------------------")
        print("Name:", _.name, "price:", _.price, "brand:", _.brand, "is_available:", _.is_available)
        print("--------------------")
    print("=================================================================")

def print_reviews():
    instances = Review.objects.all()
    print("=================================================================")
    for _ in instances:
        print("--------------------")
        print("reviewed_by:", _.reviewed_by, "reviwed_on:", _.reviwed_on, "Text:", _.text)
        print("--------------------")
    print("=================================================================")


print_products()
print_reviews()
