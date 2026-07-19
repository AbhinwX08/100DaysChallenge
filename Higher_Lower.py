import random
import HL_Data

print(HL_Data.logo_1)

print("Welcome to the Higher and Lower game!!")

def game():
    score= 0
    game_continue=True

    comp_A= random.choice(HL_Data.data_of_personalities)

    while game_continue:
        comp_B= random.choice(HL_Data.data_of_personalities)

        while comp_A==comp_B:
            comp_B= random.choice(HL_Data.data_of_personalities)
            
        print(f"Compare A: {comp_A['Name']}, age {comp_A['age']}, from {comp_A['country']}.")

        print(HL_Data.logo_2)

        print(f"Compare B: {comp_B['Name']}, age {comp_B['age']}, from {comp_B['country']}.")

        comparison= input(f"Which personality {comp_A['Name']} or {comp_B['Name']} have more followers? (A or B): ").lower()

        A_followers= comp_A['followers_millions']
        B_followers= comp_B['followers_millions']

        if A_followers>B_followers:
            correct_answer= 'a'
        else:
            correct_answer='b'
            
        if comparison== correct_answer:
            score+=1
            print(f"You are right that {comp_A['Name']} has {comp_A['followers_millions']} followers than {comp_B['Name']} has {comp_B['followers_millions']} followers ")
            print(f"Your current score: {score}")

            comp_A=comp_B

        else:
            print(f"Sorry!! You are wrong that {comp_A['Name']} has {comp_A['followers_millions']} followers AND {comp_B['Name']} has {comp_B['followers_millions']} followers ")
            print(f"Your current score: {score}")
            game_continue=False

game()