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

def inner_cond():
    game_decision= True
    while game_decision:
        if score_me==score_dealer:
            print("It's a draw!!")
        elif score_me<17 and score_dealer<17:
            print("Choose one more card to decide the winner!!")
            My_cards[2]= random.choice(possible_cards)
            Dealer_cards[2]= random.choice(possible_cards)
            if score_me>=21:
                print("Your score exceeded 21..\nYOU LOST!!!")
            elif score_me==21 and score_dealer==21:
                print("It's Draw!!")
            elif score_dealer>21:
                print("Dealer score exceeded 21..\nDEALER LOST!!!")
        else:
            game_decision=False

score_me=0
score_dealer=0

for i in My_cards:
    score_me+=My_cards[i]

if score_me>=21:
    print("Your score exceeded 21..\nYOU LOST!!!")
else:
    if score_me==21 or score_me<21:
        print("Ideal condition..\nWait for dealer to play it's move")

        Dealer_turn= int(input(f"My next card is: {random.choice(possible_cards)}"))
        My_cards.append(Dealer_turn)

        for j in Dealer_cards:
            score_dealer+=Dealer_cards[j]
        
        if score_dealer>21:
            print("DEALER LOST!!!\nDealer score exceeded 21..")
        elif score_dealer==21:
            print("It's Draw between You and Dealer..")
        elif score_dealer<21:
            inner_cond()

        elif score_me>score_dealer:
            print("You won!!")

        elif score_me<score_dealer:
            print("Dealer won!!")


