from user import User
from bank import Bank

bank = Bank()

print("Hello, Welcome to our IITP Bank.")

a = input("Please press 'Enter' to continue your banking journey.")
 

while True:

    b = int(input('''
    Choose from the below:

    1. Create a new account
    2. Continue with existing account
    3. Exit  
    ''')) #CHANGE: 1)moved initial selection menu inside the mainloop to reprompt the user after inner loop ends ,2)addition of third option to exit main loop , 33)double quotes to single quotes

    if b == 1:
        print("You have chosen to create a new account.")

        name = input("Enter your name: ")
        pin = input("Enter your pin: ")
        balance = 0

        bank.add_user(name, pin, balance)

        print("Thanks for registering, please remember your card number.")
        break

    elif b == 2:
        print("You have chosen to continue with existing account.")

        name = input("Enter your name: ")
        pin = input("Enter your pin: ")
        cd_number = input("Enter your unique card number: ")

        user = bank.check_login(name, cd_number, pin)  # CHANGE:  gave logged-in user instance
        if user:  
            print(f"Dear,{name} \nYou have logged in successfully.") 

            while True:
                a = int(input('''
Choose from the below:

1. Check Balance
2. Withdrawal Amount         
3. Deposit Amount
4. Change password
5. Exit

''')) # CHANGE: double quotes to single quotes for consistency
                if a == 1:
                    print("Your current balance is: ", user.get_balance)  # removed parentheses balance doesnt need to be called as a function

                elif a == 2:
                    user.widrawl_amount()

                elif a == 3:
                    user.deposit_amount()

                elif a == 4:
                    user.change_pin()

                elif a == 5:
                    print("You've been Logged Out Successfully!\nThanks for banking with us.") 
                    break
                    

                else:
                    print("Invalid choice. Please choose a valid option.")

        else:
            print("Invalid credentials.")
    elif b == 3:
        print("Exiting the program. Thank you for using IITP Bank.") # CHANGE : added third option to exit the program as nested loop created an infinite loop , reccomended to change loop statement from While True to is_system
        break
    else:
        print("Invalid choice. Please choose again.") # CHANGE : removed break to keep the program on loop till user chooses (3) to exit
        


