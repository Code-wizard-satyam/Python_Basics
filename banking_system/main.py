from user import User
from bank import Bank

bank = Bank()

print("Hello, Welcome to our IITP Bank.")
input("Please enter to continue your banking journey.")

while True:
    b = int(input("""
Choose from the below:

1. Create a new account
2. Continue with existing account
3. Exit

"""))
    if b == 1:
        print("You have chosen to create a new account.")
        name = input("Enter your name: ")
        pin = input("Enter your pin: ")
        balance = 0
        bank.add_user(name, pin, balance)
        print("Thanks for registering, please remember your card number.")
        continue

    elif b == 2:
        print("You have chosen to continue with existing account.")
        name = input("Enter your name: ")
        pin = input("Enter your pin: ")
        cd_number = input("Enter your unique card number: ")
        user = bank.check_login(name, cd_number, pin)
        if user:
            print("You have logged in successfully.")
            while True:
                a = int(input("""
Choose from the below:

1. Check Balance
2. Withdraw Amount
3. Deposit Amount
4. Change PIN
5. Exit

"""))
                if a == 1:
                    print("Your current balance is: ", user.get_balance)
                elif a == 2:
                    user.withdraw_amount()
                elif a == 3:
                    user.deposit_amount()
                elif a == 4:
                    user.change_pin()
                elif a == 5:
                    print("Thanks for banking with us.")
                    break
                else:
                    print("Invalid choice. Please choose a valid option.")
        else:
            print("Invalid credentials.")
        continue

    elif b == 3:
        print("Thank you for using IITP Bank.")
        break

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
