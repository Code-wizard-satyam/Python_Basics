import csv
from user import User

class Bank: #CHANGE: removed (object) as it is not needed without inheritance

    def __init__(self, filename = "bank_data.csv"):
        self.users = []
        self.filename = filename

    def add_user(self, name, pin, balance):
        dummy_cd_number = "0000"

        new_user = User(name, dummy_cd_number, pin, balance)
        new_user.create_cd_number()

        self.users.append(new_user)
        self.save_to_csv(new_user)

        print(f"User {name} added sucessfully.")

    def save_to_csv(self, user):
        with open(self.filename, mode='a', newline='') as file:  
            writer = csv.writer(file)
            writer.writerow([user.name, user._User__cd_number, user._User__pin, user.get_balance]) 
    
    def get_user_data(self):
        with open(self.filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user = User(row['Name'], row['CD Number'], int(row['PIN']), int(row['Balance']))
                self.users.append(user)

    def check_login(self, name , cd_number, pin):
        self.get_user_data()

        for user in self.users: #CHANGE:using self.users with () will call te function instead iterating over it , hence removed()
            
            if user._User__cd_number == cd_number and user._User__pin == int(pin): #CHANGE: missing double (_) in .User_pin
                return user
        print("Invalid name or PIN")
        return None

