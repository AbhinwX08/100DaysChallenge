print("Welcome to the game of treasure island!!!")
path= input("Which path would you like to take to reach the island? (e.g: left or right): ")

if path=="RIGHT" or path=="right" or path=="Right":
    print("You have taken a wrong turn and fell into the Bermuda Triangle")
else:
    print("You successfully escaped the Right route threat....")

    choice= input("Would you like to swim or take a boat to reach the the treasure island!!")

    if choice=="SWIM" or choice=="Swim" or choice=="swim":
        print("You ran out of energy!!!! Game lost")
    else:
        print("You have reached your destination your precious treasure island...")

    gate= input("There are 3 doors out of which only 1 leads to reach your treasury which door will you like to enter from? (RED/GREEN/BROWN): ")

    if gate== "RED" or gate== "Red" or gate== "red":
        print("Hurryyyyyy!!! You reached to your treasure enjoy your wealth owned by a hardwork of yours!!")
    else:
        print("You entered the wrong gate filled up with lot of snakes...\n BETTER LUCK FOR NEXT TIME!!!")

print("Moral: Hard work and Luck both decide your future rely on your hardwork and let luck work when it wanted to..")
