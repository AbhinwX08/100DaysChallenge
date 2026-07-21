import random
logo= r'''
 $$$$$$\                                                $$\   $$\                         $$\                           
$$  __$$\                                               $$$\  $$ |                        $$ |                          
$$ /  \__|$$\   $$\  $$$$$$\   $$$$$$$\  $$$$$$$\       $$$$\ $$ |$$\   $$\ $$$$$$\$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
$$ |$$$$\ $$ |  $$ |$$  __$$\ $$  _____|$$  _____|      $$ $$\$$ |$$ |  $$ |$$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ |\_$$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\  \$$$$$$\        $$ \$$$$ |$$ |  $$ |$$ / $$ / $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$ |$$ |  $$ |$$   ____| \____$$\  \____$$\       $$ |\$$$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$   ____|$$ |      
\$$$$$$  |\$$$$$$  |\$$$$$$$\ $$$$$$$  |$$$$$$$  |      $$ | \$$ |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |\$$$$$$$\ $$ |      
 \______/  \______/  \_______|\_______/ \_______/       \__|  \__| \______/ \__| \__| \__|\_______/  \_______|\__|      '''
                                                                                                                        
                                                                                                                        
                                                                                                                        
print("Welcome to the 'GUESS THE NUMBER' game")

number_chosen= random.randint(1,100)
print("Think of a number between 1 and 100")

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
            game_continue= False

        elif guessed_number!=number_chosen:
            guesses-=1
            if guessed_number>number_chosen:
                print(f"You guessed incorrectly and remaining chances of guessing is {guesses}")
                print("Guessed number is too high than actual number\n")
                
            elif guessed_number<number_chosen:
                print(f"You guessed incorrectly and remaining chances of guessing is {guesses}")
                print("Guessed number is too low than actual number\n")

        else:
            print("Enter the valid input")
            game_continue= False

    choice= input("To continue the game enter 'y' for yes and 'n' for no: ")

    if choice=='y':
        print(f"The actual number is: {number_chosen}")
        game()
    else:
        print("Thanks for playing")
        print(f"The actual number is: {number_chosen}")

game()