import random

print("Welcome to the 'GUESS THE NUMBER' game")

number_chosen= random.randint(1,101)

def game():
    difficulty= input("Choose the difficulty (e.g: 'Easy/Hard'): ").lower()
    if difficulty=='easy':
        guesses= 10
        game_control()
    elif difficulty=='hard':
        guesses=5
        game_control()
    else:
        print("Enter valid input!!")
        
def game_control():
    print(f"You have total {guesses} guesses to identify the number")
    guessed_number= int(input("Enter your number: "))
        
    game_continue= True
    while game_continue and guesses>0:
        for guessed_number in number_chosen:
            if guessed_number== number_chosen:
                print(f"You guessed correctly and won the game!!")
            elif guessed_number!=number_chosen:
                guesses-=1
                if guessed_number>number_chosen:
                    print(f"You guessed incorrectly and remaining chances of guessing is {guesses}")
                elif guessed_number<number_chosen:
                    print(f"You guessed incorrectly and remaining chances of guessing is {guesses}")
                    print("Guessed number is too low than actual number")
            else:
                print("Enter the valid input")
                game_continue= False

        choice= input("To continue the game enter 'y' for yes and 'n' for no: ")
        if choice=='n':
            game_continue=False
        elif choice=='y':
            game_continue=True
        else:
            print("Enter valid input")

game()