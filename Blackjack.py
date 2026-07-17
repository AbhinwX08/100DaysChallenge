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

possible_cards= [2,3,4,5,6,7,8,9,10,10,10,10,11]

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
        print("You win!!!")
        game_decision=False
    elif score_me>21:
        print("You went over 21, You bust and lose!!")
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

    print(f"You final card= {My_cards}, final score= {score_me}")
    print(f"Dealer final card= {Dealer_cards}, final score= {score_dealer}")
        
    if score_dealer>21:
        print("Dealer score exceeded 21..\nDealer lost!!")
    elif score_dealer==score_me:
        print("It's Draw between You and Dealer..")
    elif score_me>score_dealer:
        print("You have higher score, You win!!")
    elif score_me<score_dealer:
        print("Dealer have higher score, You lose!!")


