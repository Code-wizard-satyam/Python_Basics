import random

class User():

    used_cd_numbers = set()

    def __init__ (self, name, cd_number, pin, balance):
        self.name = name
        self.__cd_number = cd_number
        self.__pin = pin
        self.__balance = balance

    def widrawl_amount(self):
        amount = int(input("Enter the amount you want to withdraw: "))
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            print(f"${amount} has been deducted from your account.")
            self.__balance -= amount

    def deposit_amount(self):
        amount = int(input("Enter the amount you want to deposit: "))
        self.__balance += amount
        print(f"${amount} has been added to your account.")

    def change_pin(self):
        chances = 3
        while chances > 0:
            verify = int(input("Enter your current PIN: "))
            if verify == self.__pin:
                new_pin = int(input("Enter your new pin: "))
                self.__pin = new_pin
                print(f"Your new pin is {self.__pin}")
            elif chances == 0:
                print("You have exceeded the maximum number of attempts.")
            else:
                chances -= 1
                print(f"Incorrect PIN. Please try again ({chances} chances left).")

    def create_cd_number(self):
        while True:
            cd_number = str(random.randint(1000, 9999))
            if cd_number not in User.used_cd_numbers:
                User.used_cd_numbers.add(cd_number)
                self.__cd_number = cd_number
                print(f"Generated unique CD Number: {self.__cd_number}")
                break

    @property
    def get_balance(self):
        return self.__balance
    




