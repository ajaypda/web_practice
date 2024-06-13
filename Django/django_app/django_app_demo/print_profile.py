from profiles.models import Account, Message

def print_accounts():
    instances = Account.objects.all()
    print("=================================================================")
    for _ in instances:
        print("Name:", _.name, "Age:", _.age, "Country:", _.country)
        print("--------------------")
    print("=================================================================")

def print_messages():
    instances = Message.objects.all()
    print("=================================================================")
    for _ in instances:
        print("sender_name:", _.sender_name, "receiver_name:", _.receiver_name, "Text:", _.text)
        print("--------------------")
    print("=================================================================")


print_accounts()
print_messages()