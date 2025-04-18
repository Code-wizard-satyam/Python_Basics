import csv
import os
from user import User

class Bank:


    def __init__(self, filename="bank_data.csv"):
        self.users = []
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['name', 'cd_number', 'pin', 'balance'])

    def add_user(self, name, pin, balance):
        dummy_cd_number = "0000"
        new_user = User(name, dummy_cd_number, int(pin), balance)
        new_user.create_cd_number()
        self.users.append(new_user)
        self.save_to_csv(new_user)
        print(f"User {name} added successfully.")

    def save_to_csv(self, user):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([user.name, user.cd_number, user.pin, user.balance])

    def get_user_data(self):
        self.users.clear()
        with open(self.filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user = User(row['name'], row['cd_number'], int(row['pin']), int(row['balance']))
                self.users.append(user)

    def check_login(self, name, cd_number, pin):
        self.get_user_data()
        for user in self.users:
            if user.name == name and user.cd_number == cd_number and user.pin == int(pin):
                print(f"Login Successful. Thanks {name} for logging in.")
                return user
        print("Invalid name, card number, or PIN")
        return None