# myapp/management/commands/generate_fake_profile_data.py

import random
from faker import Faker
from django.utils import timezone
from django.core.management.base import BaseCommand
from profiles.models import Account, Message

fake = Faker()

class Command(BaseCommand):
    help = 'Generates fake data for Account and Message models'

    def handle(self, *args, **kwargs):
        self.generate_accounts(50)  # Generate 10 accounts
        self.generate_messages(50)  # Generate 20 messages

    def generate_accounts(self, num_accounts):
        accounts = []
        for _ in range(num_accounts):
            name = fake.name()
            age = random.randint(18, 80)
            country = fake.country()
            account = Account(name=name, age=age, country=country)
            accounts.append(account)
        Account.objects.bulk_create(accounts)
        self.stdout.write(self.style.SUCCESS(f'Generated {num_accounts} accounts.'))

    def generate_messages(self, num_messages):
        messages = []
        for _ in range(num_messages):
            sender_name = fake.name()
            receiver_name = fake.name()
            text = fake.text()
            is_deleted = random.choice([True, False])
            sent_on = timezone.make_aware(fake.date_time_this_year(), timezone.get_current_timezone())
            message = Message(sender_name=sender_name, receiver_name=receiver_name,
                              text=text, is_deleted=is_deleted, sent_on=sent_on)
            messages.append(message)
        Message.objects.bulk_create(messages)
        self.stdout.write(self.style.SUCCESS(f'Generated {num_messages} messages.'))
