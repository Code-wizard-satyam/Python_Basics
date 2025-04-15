import random as r

# Constants

set_of_cards = [1,2,3,4,5,6,7,8,9,10,10,10,10]

player_sum = 0
dealer_sum = 0

ascii_welcome = ("""
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.         .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |       | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| | _____  _____ | || |  _________   | || |   _____      | || |     ______   | || |     ____     | || | ____    ____ | || |  _________   | |       | |   ______     | || |  ____  ____  | || |      __      | || |     _____    | || |  ____  ____  | || |     ____     | |
| ||_   _||_   _|| || | |_   ___  |  | || |  |_   _|     | || |   .' ___  |  | || |   .'    `.   | || ||_   \  /   _|| || | |_   ___  |  | |       | |  |_   _ \    | || | |_   ||   _| | || |     /  \     | || |    |_   _|   | || | |_  _||_  _| | || |   .'    `.   | |
| |  | | /\ | |  | || |   | |_  \_|  | || |    | |       | || |  / .'   \_|  | || |  /  .--.  \  | || |  |   \/   |  | || |   | |_  \_|  | |       | |    | |_) |   | || |   | |__| |   | || |    / /\ \    | || |      | |     | || |   \ \  / /   | || |  /  .--.  \  | |
| |  | |/  \| |  | || |   |  _|  _   | || |    | |   _   | || |  | |         | || |  | |    | |  | || |  | |\  /| |  | || |   |  _|  _   | |       | |    |  __'.   | || |   |  __  |   | || |   / ____ \   | || |      | |     | || |    \ \/ /    | || |  | |    | |  | |
| |  |   /\   |  | || |  _| |___/ |  | || |   _| |__/ |  | || |  \ `.___.'\  | || |  \  `--'  /  | || | _| |_\/_| |_ | || |  _| |___/ |  | |       | |   _| |__) |  | || |  _| |  | |_  | || | _/ /    \ \_ | || |     _| |_    | || |    _|  |_    | || |  \  `--'  /  | |
| |  |__/  \__|  | || | |_________|  | || |  |________|  | || |   `._____.'  | || |   `.____.'   | || ||_____||_____|| || | |_________|  | |       | |  |_______/   | || | |____||____| | || ||____|  |____|| || |    |_____|   | || |   |______|   | || |   `.____.'   | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |       | |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |       | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'         '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
""")

ascii_blackjack = (''''
.------..------..------..------..------.     .------..------..------..------.
|B.--. ||L.--. ||A.--. ||C.--. ||K.--. |.-.  |J.--. ||A.--. ||C.--. ||K.--. |
| :(): || :/\: || (\/) || :/\: || :/\: ((5)) | :(): || (\/) || :/\: || :/\: |
| ()() || (__) || :\/: || :\/: || :\/: |'-.-.| ()() || :\/: || :\/: || :\/: |
| '--'B|| '--'L|| '--'A|| '--'C|| '--'K| ((1)) '--'J|| '--'A|| '--'C|| '--'K|
`------'`------'`------'`------'`------'  '-'`------'`------'`------'`------'
''')

loop = True

# Code
# Start and assigning cards

print(ascii_welcome)
inp = input("Enter to play BlackJack Game")

print(f"{ascii_blackjack} is starting")

print("Let dealer suffel cards and distribute it")

players_card = r.choices(set_of_cards, k=2)
dealers_card = r.choices(set_of_cards, k=2)

print(f"The dealer has {dealers_card[0]} and one secret card.")
print(f"You have {players_card}")

if players_card == [1,10] or players_card == [10,1]:
    print("Congrats, you won the game. It's a BlackJack.")

else:
    while loop == True:
        ask = input("Type 'h' to hit and 's' to stand.")
        if ask == "H" or ask == "h":
            loop = True
            new_card = r.choice(set_of_cards)
            players_card.append(new_card)
            length = len(players_card)
            print(f"Your new card is {new_card}.")

            for x in range(length):
                player_sum += int(players_card[x])

            if player_sum > 21:
                print("It's a burst. You lost the game.")
                loop = False

            player_sum = 0


        elif ask == "S" or ask == "s":
            loop = False

            length = len(players_card)

            for x in range(length):
                player_sum += int(players_card[x])

            dealer_sum += dealers_card[0]
            dealer_sum += dealers_card[1]

            print("It's dealers turn now")
            print(f"Dealer got {dealers_card}. Now let him get more cards.")

            while dealer_sum < 17:
                new_card = r.choice(set_of_cards)
                print(f"New card of dealer is {new_card}.")

                dealer_sum += int(new_card)
            
            if dealer_sum > 21:
                print("Dealer got a brust. You won the match.")
            
            else:
                if dealer_sum > player_sum:
                    print(f"Dealer's all cards = {dealers_card}")
                    print(f"Player's all cards = {players_card}")
                    print(f"Dealer's sum = {dealer_sum}")
                    print(f"Player's sum = {player_sum}")
                    print("Dealer won the match.")
                elif dealer_sum == player_sum:
                    print(f"Dealer's all cards = {dealers_card}")
                    print(f"Player's all cards = {players_card}")
                    print(f"Dealer's sum = {dealer_sum}")
                    print(f"Player's sum = {player_sum}")
                    print("There is a tie.")
                else:
                    print(f"Dealer's all cards = {dealers_card}")
                    print(f"Player's all cards = {players_card}")
                    print(f"Dealer's sum = {dealer_sum}")
                    print(f"Player's sum = {player_sum}")
                    print("Player won the match.")


        else:
            print("Invalid Input")
            loop = True
