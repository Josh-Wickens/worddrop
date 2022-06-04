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

WORDS = ["BALE", "RONALDO", "MESSI", "HESKEY", "BENDTNER", "BENZEMA", "BECKHAM", "SOLSKJAER",
"GERRARD", "LAMPARD", "AGUERO", "ZIDANE", "RONALDO", "NEYMAR", "ROONEY", 
"CHICHARITO", "SALAH", 
"MARADONA", "INIESTA", "HENRY", "CANTONA", "DROGBA", "LINEKER", "SILVA", 
"KOMPANY", "MARCELO", 
"VIDIC", "ERIKSON", "TERRY"]

guesses = 0
MAX_WRONG = 7
used_letters = []
wrong_answers = 0

print("\n Before we get started, I need to know your name \n")

username = input("insert name: ")

print(f"Welcome to Worddrop {username}!\n")
print("Guess the footballers name by typing out a single letter in the console. \n")
print("Too many wrong guesses and the man will hit the gallows! \n")
print("Guess one letter at a time and see if you can save him \n")

random_word = random.choice(WORDS)
current_word = random_word = "_ " * len(random_word)

print(current_word)

while wrong_answers < MAX_WRONG and current_word != random_word:
  print(HANGMANPICS[wrong_answers])
  print(f"You have used the following letter: {used_letters}")
  letter_guess = input("\n guess a letter: ")
  letter_guess = letter_guess.upper()
  print("\n You guessed:" + letter_guess)

#def show_word():
 # while wrong_answers < MAX_WRONG:
  #  print(f"you have used the letter: {used_letters}")
   # print(current_word)
  #else:
   # print(HANGMANPICS)

#def wrong_guess():

#def correct_guess():

#def lose_game():

#def win_game():

#def play game():