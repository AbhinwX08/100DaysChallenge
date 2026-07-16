gavel= (r'''           
              /~=\X~=\,
              Y)=_,~\=J7\,
              .+  `~=\_`~D
            .W'       :*+!
            @ ~\=_,   |,
           |!     `~=\_K
           @           P
          :!          |'
          Z           #W~\=_,
          5\=_,      |#P    `~=\_
          \,  `~=\_  @ ~\=_,     ~\=_,
        ._/!       ~8!     `~=\_     `~=\_
        | ~\=_,   //'           ~\=_,     ~\=_, _
        YG=\_ `~=\W,                `~=\_     `V ~\=_,
         `~=_~~==_,P                     ~\=_, |     `~=\_
             ~~\==/'                         `V_          ~\=,
  |XXXXXXXXXXXXXXXXXXXX8                        ~\=_,       |W
 P~~~~~~~~~~~~~~~~~~~~~~~V                          `~\=_, .*W
 ~V********************M~~                               `~+~M
r=+*********************==q
|                         |
K~T~T~T~T~T~T~T~T~T~T~T~T~T 
        
        ''')

print("Welcome to game of 'THE SECRET AUCTION!!'")
print(gavel)

bids= {}
game_continue= True

while game_continue:
    bidder_name= input("Enter your name: ")
    bid_price= int(input("Enter your bid: $"))

    bids[bidder_name]= bid_price

    more_bidders = input("Enter 'y' for yes to continue the game or 'n' for no to leave the game ").lower()

    if more_bidders=='n':
        game_continue=False

    elif more_bidders =='y':
        print('\n'*100)

    else:
        print("Enter valid input!!")

highest_bid = 0
winner = ""

for bidder in bids:
    bid_amount = bids[bidder]
    
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder

print(f"The winner is: {winner} with the auction price of: ${highest_bid}")