from django.core.management.base import BaseCommand
from stock.models import Stock

class Command(BaseCommand):
    help = 'Load sample Indian PSU stock data'

    def handle(self, *args, **kwargs):
        sample_data = [
            {"name": "State Bank of India", "current_price": 480.50, "volume": 10000},
            {"name": "Oil and Natural Gas Corporation", "current_price": 115.25, "volume": 15000},
            {"name": "Indian Oil Corporation", "current_price": 106.50, "volume": 20000},
            {"name": "Coal India", "current_price": 142.75, "volume": 25000},
            {"name": "Bharat Petroleum Corporation", "current_price": 360.00, "volume": 5000},
            {"name": "GAIL (India)", "current_price": 140.25, "volume": 8000},
            {"name": "Power Grid Corporation of India", "current_price": 230.50, "volume": 12000},
            {"name": "Steel Authority of India", "current_price": 89.10, "volume": 18000},
            {"name": "NTPC Limited", "current_price": 118.75, "volume": 22000},
            {"name": "Bharat Heavy Electricals", "current_price": 63.50, "volume": 14000}
        ]

        # Delete all existing records
        Stock.objects.all().delete()

        for stock in sample_data:
            Stock.objects.create(**stock)

        self.stdout.write(self.style.SUCCESS('Successfully loaded sample Indian PSU stock data'))
