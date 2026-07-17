import random

print("Welcome to the 'GUESS THE NUMBER' game")

number_chosen= random.randint(1,101)

def game():
    difficulty= input("Choose the difficulty (e.g: 'Easy/Hard'): ").lower()
    if difficulty=='easy':
        guesses= 10
        game_control(guesses)
    elif difficulty=='hard':
        guesses=5
        game_control(guesses)
    else:
        print("Enter valid input!!")
        
def game_control(guesses):
        
    game_continue= True
    print(f"You have total {guesses} guesses to identify the number")

    while game_continue and guesses>0:
        guessed_number= int(input("Enter your number: "))

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

    if choice=='y':
        game()
    else:
        print("Thanks for playing")

game()