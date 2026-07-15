print("Welcome to the game of LUCK and INTELLECT")

Hangman_stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''  
+---+
  |   |
      |
      |
      |
      |
=========
''']



player1_word = input("Think of a word so Player 2 to guess: ").lower()
lives = 6
length= len(player1_word)

display = []
for _ in range(length):
    display.append("_")

game_is_running = True

while game_is_running:
    guess = input("\nGuess a letter: ").lower()
    for position in range(length):
        letter = player1_word[position]

        if letter == guess:
            display[position] = letter
            
    if guess not in player1_word:
        lives -= 1
        print(f"Wrong guess! You lose a life. Lives remaining: {lives}")
        
    print(f"{''.join(display)}")
    
    if "_" not in display:
        game_is_running = False
        print("\nYou won! The man escaped hanging.")
    elif lives == 0:
        game_is_running = False
        print("\nYou lost! The man is hanged.")
    
    print(Hangman_stages[lives])