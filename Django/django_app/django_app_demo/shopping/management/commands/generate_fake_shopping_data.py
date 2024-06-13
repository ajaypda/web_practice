# shopping/management/commands/generate_fake_profile_data.py
import random
from faker import Faker
from django.utils import timezone
from django.core.management.base import BaseCommand
from shopping.models import Product, Review

fake = Faker()

class Command(BaseCommand):
    help = 'Generates fake data for Product and Review models'


    def handle(self, *args, **kwargs):
        self.generate_products(50)
        self.generate_review(50)

    def generate_products(self, num_products):
        prods = ["laptop", "charger", "tablet", "headset", "speaker", "mobile", "powerbank", "keyboard", "mouse"]
        brands = ["Apple","Samsung", "tata", "syska", "oppo", "jbl", "logitech", "boat", "dell" ]
        products = []
        for _ in range(num_products):
            name = random.choice(prods)
            price = random.uniform(100.0, 100000.0)
            brand = random.choice(brands)
            manufacturer = random.choice(brands)
            product_type = random.choice(["abc", "def", "xyz"])
            is_available = fake.boolean()
            product = Product(name=name, price=price, brand=brand, manufacturer=manufacturer, product_type=product_type, is_available=is_available)
            products.append(product)

        Product.objects.bulk_create(products)
        self.stdout.write(self.style.SUCCESS(f'Generated {num_products} products.'))

    def generate_review(self, num_reviews):
        reviews = ["Good to buy",
        "value for money",
        "worst product ever",
        "must buy",
        "worth to buy",
        "nice product",
        "go for it",
        "don't buy"]

        _reviews = []

        for _ in range(num_reviews):
            reviewed_by = fake.name()
            reviwed_on = timezone.make_aware(fake.date_time_this_year(), timezone.get_current_timezone())
            text = random.choice(reviews)
            review = Review(reviewed_by=reviewed_by, reviwed_on=reviwed_on, text=text)
            _reviews.append(review)

        Review.objects.bulk_create(_reviews)
        self.stdout.write(self.style.SUCCESS(f'Generated {num_reviews} reviews.'))

