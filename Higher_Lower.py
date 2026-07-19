import random
import HL_Data

print(HL_Data.logo_1)

print("Welcome to the game of Higher and Lower game!!")

def game():
    score= 0
    game_continue=True
    
    while game_continue:
        comp_A= random.choice(HL_Data.data_of_personalities)
        print(comp_A)

        print(HL_Data.logo_2)

        comp_B= random.choice(HL_Data.data_of_personalities)
        print(comp_B)

        comparison= input(f"Which personality {comp_A[0]} or {comp_B[0]} have more followers? (A or B): ").lower()

        if comp_A==comp_B:
            continue

        elif comparison=='a':
            if comp_A[3]>comp_B[3]:
                print(f"You are right!!\nPersonality {comp_A[0]} have more followers than personlaity {comp_B[0]}!!")
                score+=1
                print(f"Your Current score is: {score}")
        
            elif comp_B[3]>comp_A[3]:
                print(f"You are Wrong!!\nPersonality {comp_B[0]} have more followers than personlaity {comp_A[0]}!!")
                print(f"Your Current score is: {score}")

        elif comparison=='b':
            if comp_A[3]>comp_B[3]:
                print(f"You are right!!\nPersonality {comp_A[0]} have more followers than personlaity {comp_B[0]}!!")
                score+=1
                print(f"Your Current score is: {score}")
        
            elif comp_B[3]>comp_A[3]:
                print(f"You are Wrong!!\nPersonality {comp_B[0]} have more followers than personlaity {comp_A[0]}!!")
                print(f"Your Current score is: {score}")
                
        else:
            print("Enter valid input!!")

        Again= input("Do you want to play again?\nEnter 'y' for yes and 'n' for no: ").title()
        if Again=='N':
            game_continue=False
        elif Again=='Y':
            game_continue=True
        else:
            print("Enter valid input")

game()