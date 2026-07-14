import random

rock= ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper= ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors= ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
list=[rock, Paper, Scissors]

User_choice= int(input("Enter your move (0 for rock, 1 for paper and 2 for scissors): \n"))

if User_choice>=3 or User_choice<0:
    print("Enter valid number")

else:
    print("Users choice!!")
    print(list[User_choice])

    computer_choice= random.randint(0,2)
    print("Computers Choice!!")
    print(list[computer_choice])
    
    if User_choice==computer_choice:
        print("It's a draw!!")
    elif User_choice==0 and computer_choice==1:
        print("You lose!!")
    elif User_choice==0 and computer_choice==2:
        print("You won!!")
    elif User_choice==1 and computer_choice==0:
        print("You won!!")
    elif User_choice==1 and computer_choice==2:
        print("You lose!!")
    elif User_choice==2 and computer_choice==0:
        print("You lose!!")
    elif User_choice==2 and computer_choice==1:
        print("You Won!!")



