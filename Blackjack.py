import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
print("Welcome to the Casino, Let's play 'BlackJack!!'")

balance= 1000
possible_cards= [2,3,4,5,6,7,8,9,10,10,10,10,11]

game_continue=True
while game_continue:
    print(f"Your current balance is: ${balance}")

    if balance<=0:
        print("You ran out of money, No more bet can be done!!\nGame over")
        break

    bet= int(input("Enter the bet you wanted to put for this move?: $"))

    if bet>balance:
        print("You don't have that much balance to make such big bet...")
        bet= balance

    My_cards= []
    Dealer_cards=[]

    for i in range(2):
        My_cards.append(random.choice(possible_cards))
        Dealer_cards.append(random.choice(possible_cards))

    game_decision= True

    while game_decision:
        score_me= sum(My_cards)
        score_dealer= sum(Dealer_cards)
    
        print(f"Your cards= {My_cards}, Your score= {score_me}")
        print(f"Dealer cards= {Dealer_cards[0]}")

        if score_me==21:
            game_decision=False

        elif score_me>21:
            game_decision=False
        else:
            pass_card= input("Type 'y' for yes to take another card and 'n' for no: ")
            if pass_card=='y':
             My_cards.append(random.choice(possible_cards))
            else:
                game_decision=False

    if score_me<=21:
        while sum(Dealer_cards)<17:
            Dealer_cards.append(random.choice(possible_cards))

        score_dealer= sum(Dealer_cards)

        print(f"Your final card= {My_cards}, final score= {score_me}")
        print(f"Dealer final card= {Dealer_cards}, final score= {score_dealer}")
        
        if score_me>21:
            print("Your score exceeded 21..\nYou lose!!")
            balance-=bet

        if score_dealer>21:
            print("Dealer score exceeded 21..\nDealer lose!!")
            balance+=bet

        elif score_dealer==score_me:
            print("It's Draw between You and Dealer..")

        elif score_me>score_dealer:
            print("You have higher score, You win!!")
            balance+=bet

        elif score_me<score_dealer:
            print("Dealer have higher score, You lose!!")
            balance-=bet

        if balance>0:
            play_again= input("Do you want to play again....\nEnter 'y' for yes and 'n' for no: ")
            if play_again=='n':
                game_continue=False
                print(f"Your current balance is: {balance}\nThanks for playing!!")
