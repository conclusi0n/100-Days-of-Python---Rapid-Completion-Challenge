import random

# ASCII art stages
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

# Word list
word_list = ["python", "hangman", "coding", "developer", "algorithm"]
word = random.choice(word_list)
guessed_letters = ["_"] * len(word)
lives = 6
guessed = []

# Game loop
while "_" in guessed_letters and lives > 0:
    print(" ".join(guessed_letters))
    print(stages[lives])
    
    guess = input("Guess a letter: ").lower()
    
    if not guess.isalpha() or len(guess) != 1:
        print("Invalid input. Please guess a single letter.")
        continue

    if guess in guessed:
        print("You already guessed that letter!")
        continue

    guessed.append(guess)

    if guess in word:
        for index in range(len(word)):
            if word[index] == guess:
                guessed_letters[index] = guess
    else:
        print("Incorrect guess!")
        lives -= 1

# End game
if "_" not in guessed_letters:
    print("You win! The word was:", word)
else:
    print(stages[0])  # Show final Hangman stage
    print("You lose! The word was:", word)
