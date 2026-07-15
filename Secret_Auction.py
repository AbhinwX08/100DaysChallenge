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

print("Welcome to THE SECRET AUCTION!!")
print(gavel)

auctioneer= {}
game_continue= True

while game_continue:
    Name= input("Enter your name: ")
    Price= int(input("Enter the price: $"))

    auctioneer[Name]=Price

    game= input("Enter 'y' for yes to continue the game or 'n' for no to leave the game ").lower()

    if game=='n':
        game_continue=False

    elif game=='y':
        print('\n'*100)

    else:
        print("Enter valid input!!")

highest_bid = 0
winner = ""
  
for bidder in auctioneer:
    bid_amount = auctioneer[bidder]
    
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder

print(f"The winner is: {winner} with the auction price of: ${highest_bid}")