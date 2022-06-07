import random

HANGMANPICS = ['''

   +---+
   |   |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |

=========''']

WORDS = ["BALE", "RONALDO", "MESSI", "HESKEY", "BENDTNER", "BENZEMA", "BECKHAM", "SOLSKJAER", "GERRARD", "LAMPARD", "AGUERO", "ZIDANE", "RONALDO", "NEYMAR",
         "ROONEY", "CHICHARITO", "SALAH", "MARADONA", "INIESTA", "HENRY", "CANTONA", "DROGBA", "LINEKER", "SILVA", "KOMPANY", "MARCELO", "VIDIC", "ERIKSON", "TERRY"]

guesses = 0

MAX_WRONG = 7

used_letters = []

wrong_answers = 0

print("\n Before we get started, I need to know your name \n")

username = input("insert name: ")
print(f"Welcome to Worddrop {username}!")
print("\nGuess the footballers name by typing out a single letter in the console. \n")
print("Too many wrong guesses and the man will hit the gallows! \n")
print("Guess one letter at a time and see if you can save him \n")

random_word = random.choice(WORDS)
current_word = "_ " * len(random_word)

print(current_word)

while wrong_answers != 6 and current_word != random_word:
    print(HANGMANPICS[wrong_answers])
    print(f"You have used the following letter: {used_letters}")

    letter_guess = input("\n guess a letter: ")
    letter_guess = letter_guess.upper()
    print("\n You guessed:" + letter_guess)

    while letter_guess in used_letters:
        print(f"you have already guessed this letter: {letter_guess}\n")
        print("Guess a different letter\n")
        letter_guess = input("\n guess a letter: ")
        letter_guess = letter_guess.upper()
        print("\n You guessed:" + letter_guess)

    used_letters.append(letter_guess)

    if letter_guess in current_word:
        print("Correct!")
        new_current_guess = ""
        for letter in range(len(current_word)):
            if letter_guess == current_word[letter]:
                new_current_guess += letter_guess
            else:
                new_current_guess += current_word[letter]

        current_word = new_current_guess

    # for letter in used_letters:
    #   if letter == letter_guess:
    #      print(
    #         "you have already guessed this letter. Please try and guess a different letter")


# guess_letter(letter)
# run_game()
# def show_word():
# while wrong_answers < MAX_WRONG:
#  print(f"you have used the letter: {used_letters}")
# print(current_word)
# else:
# print(HANGMANPICS)

# def wrong_guess():

# def correct_guess():

# def lose_game():

# def win_game():

# def play game():
