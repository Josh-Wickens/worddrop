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

print("Welcome to Worddrop!")

random_word = random.choice(WORDS)
current_word = random_word = "_" * len(random_word)

print(current_word)